<script lang="ts">
	import Download3d from './Download3d.svelte';
	import GridLine from './GridLine.svelte';
	import UploadImg from './UploadImg.svelte';

	let uploaded: boolean = false;
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<UploadImg />
	{#if uploaded}
		<Download3d />
		<GridLine />
	{/if}
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}
</style>
