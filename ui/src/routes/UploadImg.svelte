<!-- upload an image -->

<script lang="ts">
	import axios from 'axios';

	let files: FileList | null = null;
	let error: string | null = null;
	let vertical: number | null = null;
	let isUploaded: boolean = false;

	function handleVertical(event: Event) {
		const target = event.target as HTMLInputElement;
		vertical = Number(target.value);
		console.log(vertical);
	}

	async function submit() {
		const config = {
			headers: {
				'content-type': 'multipart/form-data'
			}
		};
		const formData = new FormData();
		if (files) {
			formData.append('file', files[0]);
			console.log(files[0]);
		}
		axios
			.post(
				`http://127.0.0.1:8000/upload/image?vertical=${vertical}&area_threshold=1000`,
				formData,
				config
			)
			.then(function (response) {
				console.log(response);
				isUploaded = true;
			})
			.catch(function (error) {
				console.log(error);
				error = error;
			});
	}
</script>

<h2>写真をアップロード</h2>

{#if error}
	<p class="error">{error}</p>
{/if}

<form on:submit|preventDefault={submit}>
	<label>
		縦の長さ（cm）
		<input name="vertical" type="number" on:change={handleVertical} required />
	</label>
	<input accept=".jpg, .jpeg, .png" type="file" bind:files />
	<button type="submit">送信</button>
</form>
{#if isUploaded}
	<img class="result" src="http://localhost:8000/load/image" alt="result" />
{/if}

<style>
	.error {
		color: red;
	}

	.result {
		width: 100%;
	}
</style>
