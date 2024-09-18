<script lang="ts">
	import { onMount } from "svelte";
	import "./app.css";
	import Header from "./components/Header.svelte";
	import Graph from "./components/Graph.svelte";
	import type { Link, Node } from "./types";
	import { Backend } from "./backend";
	import type { WithinSimilarResponse } from "./backend";

	let d: WithinSimilarResponse;
	let links: Link[] = [];
	let nodes: Node[] = [];
	onMount(async () => {
		d = await Backend.withinSimilar();
		const res = convertFormat(d);
		links = res[0];
		nodes = res[1];
	});

	function convertFormat(data: WithinSimilarResponse): [Link[], Node[]] {
		let nodes: Node[] = [];
		let links: Link[] = [];

		for (const n of data.nodes) {
			nodes.push({ id: n, group: 1 });
		}
		for (const e of data.edges) {
			const [source, target, value] = e;
			//@ts-ignore
			if (value > 0.1) {
				//@ts-ignore
				links.push({ source, target, value, weight: value });
			}
		}

		//@ts-ignore
		const results = detectCommunities(data.nodes, links);
		for (const n of nodes) {
			n["group"] = results[n.id];
		}

		return [links, nodes];
	}

	function detectCommunities(
		nodes: string[],
		links: { source: string; target: string; weight: number }[]
	): Record<string, number> {
		//@ts-ignore
		return jLouvain().nodes(nodes).edges(links)();
	}
</script>

<Header />
<main>
	{#if links.length > 0 && nodes.length > 0}
		<Graph width={1000} height={800} {links} {nodes} />
	{/if}
</main>

<style>
</style>
