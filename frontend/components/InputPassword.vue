<template>
	<div class="input">
		<input 
			type="password" 
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
	name: 'InputPassword',
	props: {
		name: String,
		placeholder: String,
		value: String,
		disabled: Boolean
	}
}

</script>