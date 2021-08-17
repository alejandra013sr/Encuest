<template>
	<div class="login">
		<main class="login__main">
			<div class="login__title">
				<span>Inicia sesion</span>
				<span>para continuar</span>
			</div>
			<form class="login__form" @submit.prevent>
				<InputEmail v-model="email" name="email" placeholder="Correo" />
				<InputPassword v-model="pass" name="password" placeholder="Contraseña" />
				<Button class="button--backgroundGradient" @click="login">Log in</Button>
			</form>	
			<div class="login__links">
				<Button class="button--borderGradient">Google</Button>
				<Button class="button--borderGradient">Facebook</Button>
			</div>
		</main>
		<footer class="login__footer">
			<span>¿No tienes una cuenta?.</span>
			<b>
				<NuxtLink to='/register' href="#">Registrate</NuxtLink>
			</b>
		</footer>

	</div>
</template>
<script>
	
export default {
	name: 'Login',
	transition: 'auth',
	layout: 'home',
	data(){
		return {
			email: '',
			pass: ''
		}
	},
	methods: {
		async login(){
			const resauth = await this.$auth.loginWith('local', {
				data: {
					email: this.email,
					password: this.pass
				}
			});
			console.log(resauth);
			this.$router.push('/dashboard');
		}
	}
}

</script>