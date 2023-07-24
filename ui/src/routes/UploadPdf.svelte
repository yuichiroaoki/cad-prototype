<!-- upload a pdf file -->

<script lang="ts">
	import axios from 'axios';

	let files: FileList | null = null;
	let error: string | null = null;

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
			.post('http://127.0.0.1:8000/upload/pdf', formData, config)
			.then(function (response) {
				console.log(response);
			})
			.catch(function (error) {
				console.log(error);
				error = error;
			});
	}
</script>

<h2>Upload a PDF</h2>

{#if error}
	<p class="error">{error}</p>
{/if}

<form on:submit|preventDefault={submit}>
	<input accept="application/pdf" type="file" bind:files />
	<button type="submit">Upload</button>
</form>

<style>
	.error {
		color: red;
	}
</style>
