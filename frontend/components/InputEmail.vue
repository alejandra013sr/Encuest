<template>
	<div class="input">
		<input 
			type="email" 
			:name="name" 
			:placeholder="placeholder"
			:value="value"
			@input="$emit('input', $event.target.value)"
			:disabled="disabled"
		>
	</div>
</template>
<script>
export default {
	name: 'InputEmail',
	props: {
		name: String,
		placeholder: String,
		value: String,
		disabled: Boolean
	}
}

</script>