//let d3 = require("d3");

let signalScale = d3.scaleOrdinal()
    .domain(["GO", "STOP", "READY", "SLOW_DOWN"])
    .range(["green", "red", "yellow", "orange"]);

function drawIntersection(intersection, view) {
    let viewWidth = view.attr("width");
    let viewHeight = view.attr("height");

    let lines = [];
    for (lane of intersection.lanes) {
        lines.push(lane.side1);
        lines.push(lane.side2);
    }

    let maxX = d3.max(lines, (d) => d3.max([d.p1.x, d.p2.x]));
    let maxY = d3.max(lines, (d) => d3.max([d.p1.y, d.p2.y]));
    let minX = d3.min(lines, (d) => d3.min([d.p1.x, d.p2.x]));
    let minY = d3.min(lines, (d) => d3.min([d.p1.y, d.p2.y]));

    let xScale = d3.scaleLinear()
        .domain([minX, maxX])
        .range([0, viewWidth]);

    let yScale = d3.scaleLinear()
        .domain([minY, maxY])
        .range([0, viewHeight]);

    let mapLine = view.select("#intersection").selectAll("line").data(lines);
    mapLine.enter()
        .append("line")
        .attr("x1", (d) => xScale(d.p1.x))
        .attr("y1", (d) => yScale(d.p1.y))
        .attr("x2", (d) => xScale(d.p2.x))
        .attr("y2", (d) => yScale(d.p2.y))
        .attr("stroke", "black");

    let laneEnds = []; // Only lane end with traffic light
    for (laneEnd of intersection.laneEnds) {
        if (laneEnd.trafficLight !== null) {
            laneEnds.push(laneEnd);
        }
    }
    let laneLines = view.select("#traffic-lights").selectAll("line")
        .data(laneEnds, (laneEnd) => laneEnd.trafficLight.id);

    laneLines.enter()
        .append("line")
        .attr("x1", (laneEnd) => xScale(laneEnd.boundary.p1.x))
        .attr("y1", (laneEnd) => yScale(laneEnd.boundary.p1.y))
        .attr("x2", (laneEnd) => xScale(laneEnd.boundary.p2.x))
        .attr("y2", (laneEnd) => yScale(laneEnd.boundary.p2.y))
        .attr("stroke-width", "3px")
        .attr("stroke", (laneEnd) => signalScale(laneEnd.trafficLight.signal));

    return {
        "width": viewWidth,
        "height": viewHeight,
        "xScale": xScale,
        "yScale": yScale
    }
}

function updateTraffic(trafficLights, view) {
    let trafficLines = view.select("#traffic-lights")
        .selectAll("line")
        .data(trafficLights)
        .join(
            enter => enter,
            update => update.attr("stroke", (d) => signalScale(d.signal))
        );
}

function drawVehicle(vehicles, view, intersctionView, transitionConfig) {
    let xScale = intersctionView.xScale;
    let yScale = intersctionView.yScale;

    let vehicleCircles = view.select("#vehicles")
        .selectAll("circle")
        .data(vehicles, (vehicle) => vehicle.id);

    vehicleCircles.join(
        enter => {
            enter.append("circle")
                .attr("cx", (vehicle) => xScale(vehicle.p.x))
                .attr("cy", (vehicle) => yScale(vehicle.p.y))
                .attr("r", "5px")
                .attr("fill", "blue");
        },

        update => {
            update.transition(transitionConfig)
                .duration(200)
                .attr("cx", (vehicle) => xScale(vehicle.p.x))
                .attr("cy", (vehicle) => yScale(vehicle.p.y))
        },

        exit => exit.remove()
    );
}

function update(updateTimer, view, intersectionView) {
    let transitionConfig = d3.transition()
        .duration(250)
        .ease(d3.easeLinear);
    d3.json("vehicles/0/")
        .then((data) => drawVehicle(data, view, intersectionView, transitionConfig))
        .catch(error => updateTimer.stop());
    d3.json("traffic-lights/0/")
        .then((data, error) => updateTraffic(data, view))
        .catch(error => updateTimer.stop());
}

document.addEventListener("DOMContentLoaded", function (e) {
    d3.json("intersection/0/").then((data) => {
        if (data !== null) {
            let trafficView = d3.select("#traffic");
            let intertsectionView = drawIntersection(data, trafficView);
            let updateTimer = d3.interval(() => update(updateTimer, trafficView, intertsectionView), 200);
        }
    });
});