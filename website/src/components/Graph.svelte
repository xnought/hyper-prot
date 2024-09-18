<script lang="ts">
	import * as d3 from "d3";
	import { onMount } from "svelte";
	import type { Link, Node } from "../types";

	let svgEl, svg, sim;
	export let width = 1600;
	export let height = 1000;
	export let nodes: Node[] = [
		{ id: "a", group: 1 },
		{ id: "b", group: 1 },
		{ id: "c", group: 1 },
		{ id: "d", group: 1 },
		{ id: "e", group: 1 },
	];
	export let links: Link[] = [
		{ source: "a", target: "b", value: 4 },
		{ source: "b", target: "c", value: 1 },
		{ source: "e", target: "d", value: 1 },
		{ source: "c", target: "a", value: 4 },
	];
	let selected = {};

	/**
	 * most of this is from [ObservableHQ](https://observablehq.com/@d3/disjoint-force-directed-graph/2?intent=fork)
	 */
	function graph(svg: SVGElement, nodes: unknown, links: unknown) {
		const xScale = (x) => x;
		const yScale = (y) => y;
		sim = d3
			.forceSimulation(nodes)
			.force(
				"link",
				d3.forceLink(links).id((d) => d.id)
				// .distance(70)
			)
			.force(
				"charge",
				d3.forceManyBody()
				// .strength(-30)
			)
			.force("x", d3.forceX())
			.force("y", d3.forceY())
			.force("center", d3.forceCenter(width / 2, height / 2))
			.on("tick", update);

		// Add a line for each link, and a circle for each node.
		const link = svg
			.append("g")
			.attr("stroke", "#999")
			.selectAll("line")
			.data(links)
			.join("line")
			.attr("stroke-opacity", function (d) {
				return 0.2;
			})
			.attr("stroke-width", (d) => d.value * 3);

		const node = svg
			.append("g")
			.attr("stroke", "black")
			.attr("stroke-width", 1.5)
			.selectAll("circle")
			.data(nodes)
			.join("circle")
			.attr("r", (d) => 5)
			.attr(
				"fill",
				(d) =>
					d3.schemeTableau10.concat(d3.schemeCategory10)[d.group % 20]
			)
			.on("click", (e, d) => {
				selected = d;
			});

		function update() {
			const x = "x";
			const y = "y";
			// const x = "cx";
			// const y = "cy";
			link.attr("x1", function (d) {
				return xScale(d.source[x]);
			})
				.attr("y1", function (d) {
					return yScale(d.source[y]);
				})
				.attr("x2", function (d) {
					return xScale(d.target[x]);
				})
				.attr("y2", function (d) {
					return yScale(d.target[y]);
				});

			node.attr("cx", function (d) {
				return xScale(d[x]);
			}).attr("cy", function (d) {
				return yScale(d[y]);
			});
		}

		node.call(
			d3
				.drag()
				.on("start", dragstarted)
				.on("drag", dragged)
				.on("end", dragended)
		);

		// Reheat the simulation when drag starts, and fix the subject position.
		function dragstarted(event) {
			if (!event.active) sim.alphaTarget(0.3).restart();
			event.subject.fx = event.subject.x;
			event.subject.fy = event.subject.y;
		}

		// Update the subject (dragged node) position during drag.
		function dragged(event) {
			event.subject.fx = event.x;
			event.subject.fy = event.y;
		}

		// Restore the target alpha so the simulation cools after dragging ends.
		// Unfix the subject position now that it’s no longer being dragged.
		function dragended(event) {
			if (!event.active) sim.alphaTarget(0);
			event.subject.fx = null;
			event.subject.fy = null;
		}

		update();
	}

	onMount(async () => {
		svg = d3.select(svgEl);
		graph(svg, nodes, links);
	});
</script>

<div>
	<svg bind:this={svgEl} {width} {height} />
	{JSON.stringify(selected, null, 4)}
</div>

<style>
	svg {
		outline: lightgrey 1px dashed;
		overflow: visible;
	}
</style>
