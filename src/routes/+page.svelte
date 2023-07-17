<script>
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';

	import { Canvas, InteractiveObject, OrbitControls, T } from '@threlte/core';
	import { spring } from 'svelte/motion';
	import { degToRad } from 'three/src/math/MathUtils';

	const scale = spring(1);
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>
		<span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span>

		to your new<br />SvelteKit app
	</h1>

	<h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2>

	<Counter />

	<div>
		<Canvas>
			<T.PerspectiveCamera makeDefault position={[10, 10, 10]} fov={24}>
				<OrbitControls maxPolarAngle={degToRad(80)} enableZoom={false} target={{ y: 0.5 }} />
			</T.PerspectiveCamera>

			<T.DirectionalLight castShadow position={[3, 10, 10]} />
			<T.DirectionalLight position={[-3, 10, -10]} intensity={0.2} />
			<T.AmbientLight intensity={0.2} />

			<!-- Cube -->
			<T.Group scale={$scale}>
				<T.Mesh position.y={0.5} castShadow let:ref>
					<!-- Add interaction -->
					<InteractiveObject
						object={ref}
						interactive
						on:pointerenter={() => ($scale = 2)}
						on:pointerleave={() => ($scale = 1)}
					/>

					<T.BoxGeometry />
					<T.MeshStandardMaterial color="#333333" />
				</T.Mesh>
			</T.Group>

			<!-- Floor -->
			<T.Mesh receiveShadow rotation.x={degToRad(-90)}>
				<T.CircleGeometry args={[3, 72]} />
				<T.MeshStandardMaterial color="white" />
			</T.Mesh>
		</Canvas>
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}

	div {
		height: 100%;
		width: 100%;
	}
</style>
