<template>

	<div class="w-full footer">
		<div class="box py-20 flex justify-end">
			<div class="w-1/3 items-center">
				<LogoComponent class="mb-5"/>
				<SocialIconsComponent class="ml-0"/>
			</div>
			<div class="w-1/3">
				<div class="title">Chácara recanto dos pássaros </div>
				<div>
					Lorem ipsum dolor sit amet, consectetur adipiscing elit. In aliquam libero sit amet finibus scelerisque. Vestibulum et massa aliquam, mollis ligula auctor, fringilla nisl. Nam id iaculis lectus.
				</div>
			</div>
			<div class="ml-auto w-1/6">
				<div class="title">Entre em contato </div>
				<div class="group">
					<div>
            			<font-awesome-icon :icon="['fas', 'envelope']" />
					</div>
					<p> 
						adilsonpol@hotmail.com
					</p>
				</div>
				<div class="group">
					<div>
            			<font-awesome-icon :icon="['fas', 'phone']" />
					</div>
					<p> 
						11 99896-1438
					</p>
				</div>
				<div class="group">
					<div>
            			<font-awesome-icon :icon="['fas', 'map-marker']" />
					</div>
					<p> 
						Suzano
					</p>
				</div>
			</div>
		</div>
		<div>
			© 2020. All rights reserved.
		</div>
	</div>
</template>

<script>
import SocialIconsComponent from './../home/SocialIconsComponent.vue'
import LogoComponent from './../home/LogoComponent.vue'
export default {
	components: {
		SocialIconsComponent,
		LogoComponent,
	}
}
</script>


<style lang="scss">
@import "./style.scss";

</style>
