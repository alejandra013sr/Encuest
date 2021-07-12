<template>
	<div class="input">
		<input type="email" :name="name" :placeholder="placeholder">
	</div>
</template>
<script>
export default {
	name: 'InputEmail',
	props: {
		name: String,
		placeholder: String
	}
}

</script>