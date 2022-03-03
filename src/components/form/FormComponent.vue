<template>
	<div class="w-full h-screen form">
		<div class="box-screen flex flex-col items-center">
			<div class="w-full mt-auto">
				<p class="partners-title mb-10 mt-auto">
					Faça a sua reserva
				</p>
			</div>
			<div class="w-full flex">
				<div class="w-1/2 mr-10">
					<div class="input">
						<input type="text" name="name"  class="input__field"/>
						<label for="name" class="input__label">Nome</label>
					</div>

					<div class="input">
						<input type="text" name="email"  class="input__field"/>
						<label for="email" class="input__label" >E-mail</label>
					</div>

					<div class="input">
						<input type="text" name="telephone"  class="input__field"/>
						<label for="telephone" class="input__label" placeholder="Nome">Telefone</label>
					</div>

				</div>
				<div class="w-1/2 flex flex-col">
					<div class="w-full flex">
						<div class="input w-1/2 mr-2 ">
							<input type="text" name="start_date"  class="input__field "/>
							<label for="start_date" class="input__label" placeholder="Nome">Data Inicial</label>
						</div>

						<div class="input w-1/2">
							<input type="text" name="final_date"  class="input__field"/>
							<label for="final_date" class="input__label" placeholder="Nome">Data Final</label>
						</div>
					</div>

					<div class="input w-full">
						<textarea
							name="message"
							class="input__field"
							cols="30"
							rows="10"
						></textarea>
						<label for="message" class="input__label">Mensagem</label>
					</div>
				</div>
			</div>
			<div class="w-full mb-auto text-right">
				<button class="btn-green ml-auto py-10 px-20 font-sm">Verificar datas</button>
			</div>
		</div>
	</div>
</template>


<style lang="scss">
@import "./style.scss";
</style>
