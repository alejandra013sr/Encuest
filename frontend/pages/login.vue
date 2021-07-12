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
				<InputEmail name="email" placeholder="Correo" />
				<InputPassword name="password" placeholder="Contraseña" />
				<Button class="button--backgroundGradient">Log in</Button>
			</form>	
			<div class="login__links">
				<Button class="button--borderGradient">Google</Button>
				<Button class="button--borderGradient">Facebook</Button>
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