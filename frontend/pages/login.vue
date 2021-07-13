<template>
	<div class="login">
		<header class="login__header">
			<div class="login__logo">
				<Logo width="80px" background="horizontalGradient" />
			</div>
			<div class="login__title">
				<span>Inicia sesión </span>
				<span>para continuar</span>
			</div>
		</header>
		<main class="login__main">
			<form class="login__form" @submit.prevent>
				<InputEmail v-model="email" name="email" placeholder="Correo" />
				<InputPassword v-model="pass" name="password" placeholder="Contraseña" />
				<Button class="button--backgroundGradient" @click="login">Log in</Button>
			</form>	
			<div class="login__links">
				<Button class="button--borderGradient">Google</Button>
				<Button class="button--borderGradient">Facebook</Button>
				<div>{{email}}</div>
			</div>
		</main>
		<footer class="login__footer">
			<span>¿No tienes una cuenta?.</span>
			<b>
				<a href="#">Registrate</a>
			</b>
		</footer>

	</div>
</template>
<script>
	
export default {
	name: 'Login',
	data(){
		return {
			email: '',
			pass: ''
		}
	},
	methods: {
		async login(){
			const res = await this.$axios.$post('http://localhost:8000/profile/users/', {
				data: {
					name: 'Prueba',
					email: this.email,
					password: this.pass
				}
			});
			console.log(res);
		}
	}
}

</script>