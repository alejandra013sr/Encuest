<template>
	<div class="login">
		<main class="login__main">
			<div class="login__title">
				<span>Inicia sesion</span>
				<span>para continuar</span>
			</div>
			<form class="login__form" @submit.prevent>
				<InputEmail 
					v-model="creds.email" 
					name="email" 
					placeholder="Correo" 
					:disabled="isLoading"
				/>
				<InputPassword 
					v-model="creds.pass" 
					name="password" 
					placeholder="Contraseña" 
					:disabled="isLoading"
				/>
				<Button 
					class="button--backgroundGradient" 
					@click="login"
					:disabled="isLoading"
				>Log in</Button>
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

import authMixin from '~/mixins/auth.mixin'
import { STATUS_INITIAL, STATUS_LOADING } from '~/utils/statusConstants'

export default {
	name: 'Login',
	transition: 'auth',
	layout: 'home',
	mixins: [authMixin],
	data(){
		return {
			creds: {
				email: '',
				pass: ''
			}
		}
	},
	methods: {
		async login(){
			const validation = this.validateForm();
			
			if(!validation){

				this.$notify({
					type: 'warnning',
					// title: 'Error',
					text: 'Debes llenar todos los campos.'
				});

				this.currentStatus = STATUS_INITIAL;
				return;
			}

			try {

				await this.$auth.loginWith('local', {
					data: {
						email: this.creds.email,
						password: this.creds.pass
					}
				});

				this.$router.push('/dashboard');

			} catch (e){

				this.currentStatus = STATUS_INITIAL;

				const error = e.toJSON();
				this.$notify({
					type: 'error',
					title: 'Error',
					text: error.message

				});
			}
		}
	}
}

</script>