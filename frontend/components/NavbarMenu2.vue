<template>
  <div class="navbar-menu2__wrapper">
    <div class="navbar-menu2">
      <div class="navbar-menu2__circle">
        <div class="navbar-menu2__bg" ref="navbarBg">
          <div class="circle" ref="navbarCircle">
            <font-awesome-icon 
              :icon="currentIcon"
            />
          </div>
        </div>
      </div>
      <div 
        class="navbar-menu2__item" 
        v-for="(option, index) in options" 
        :key="`n${index}`"
      >
        <NuxtLink 
          class="navbar-menu2__icon"
          :data-in="index"
          :to="option.link"
        >
          <font-awesome-icon 
            @click="click(index, option, $event)"
            :icon="['fas', option.icon]" 
            color="#bdbdbd"
          />
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
<script>

import getTranslateValues from '~/helpers/getTranslateValues'

export default {
  name: 'NavbarMenu2',
  data(){
    return {
      options: [
        { icon: 'user', link: '/profile' },
        { icon: 'images', link: '/dashboard' },
        { icon: 'home', link: '/dashboard' },
        { icon: 'bolt', link: '/dashboard' },
        { icon: 'plus', link: '/add-image' }
      ],
      currentIcon: 'home',
      previousOptionIndex: 3
    }
  },
  methods: {
    click(index, option, e){
      const optionElements = Array.from(document.querySelectorAll('.navbar-menu2 .navbar-menu2__item'));
      console.log(optionElements);
      const previousOption = optionElements[this.previousOptionIndex];
      const target = optionElements[index];
      
      // Obtenemos los datos de el circulo y el elemento
      const targetDataPosition = target.getBoundingClientRect();
      // Calculamos la posicion del centro de la opcion target
      const targetCenter = targetDataPosition.left + (targetDataPosition.width / 2);
      // console.log(`El centro de la opcion que se clicleo esta en ${targetCenter}`);

      const bgDataPosition = this.$refs.navbarBg.getBoundingClientRect();
      const bgCenter = bgDataPosition.left + (bgDataPosition.width / 2);
      // console.log(`El centro del circulo esta en ${bgCenter}`);

      const { x } = getTranslateValues(this.$refs.navbarBg);

      const newBgCenter = targetCenter - bgCenter + parseInt(x);
      // console.log(`Transladando el circulo a ${newBgCenter}`);
      
      // otra forma
      const startPosition = parseInt(x);
      const middlePosition = (newBgCenter + parseInt(x))/2;
      console.log(middlePosition);
      const endPosition = newBgCenter;
      const dis = endPosition - startPosition;
      const keyframes = [
        { transform : `translateX(0px) translateY(0)` },
        { transform : `translateX(0px) translateY(50px)` },
        { transform : `translateX(${(Math.sign(dis) * -20)}px) translateY(50px)` },
        { transform : `translateX(0px) translateY(0)` }
      ];
      console.log(keyframes);
      const circleAnimation = this.$refs.navbarCircle.animate(keyframes,{
        duration: 1200,
        fill: 'forwards',
        easing: 'ease'
      });
      const options = optionElements.map(option => option.firstChild);
      let optionsToAminate = options.filter(option => {
        const indexOption = parseInt(option.dataset.in);
        // console.log( `ìndex: ${indexOption} >= prev: ${this.previousOptionIndex} && index: ${indexOption} <= new: ${index}`);
        if(this.previousOptionIndex < index){
          if(indexOption >= this.previousOptionIndex && indexOption <= index) return option;
        } else if(this.previousOptionIndex > index){
          if(indexOption <= this.previousOptionIndex && indexOption >= index) return option;
        }
      });
      // console.log(optionsToAminate.map(op => op.dataset.in));
      if(this.previousOptionIndex > index){
        optionsToAminate = optionsToAminate.sort((a,b) => parseInt(b.dataset.in) - parseInt(a.dataset.in));
      }
      // console.log(optionsToAminate.map(op => op.dataset.in));
      optionsToAminate.forEach((option, i) => {
        // console.log(option);
        // console.log(300 - ((Math.abs(index - this.previousOptionIndex) - 4) * 100));
        const delay = i;
        const opacityStart = i === 0 ? '0' : '1';
        const opacityEnd = i === (optionsToAminate.length - 1) ? '0' : '1';
        const keyframes = [
          { transform: 'translateY(0)', opacity: opacityStart },
          { transform: 'translateY(32.5px)' },
          { transform: 'translateY(0)',  opacity: opacityEnd }
        ];
        option.animate(
          keyframes,
          {
            duration: 1200 - ((Math.abs(index - this.previousOptionIndex) - 4) * 40),
            delay: (delay * 100 ) - (delay * 50),
            fill: 'forwards',
            easing: 'ease'
          }
        );
      });
      setTimeout(() => {
        const backgroundPosBase = (100 / (optionElements.length + 1)) * (index + 1);
        previousOption.classList.remove('hide');
        // console.log('removiendo la clase hide de :');
        // console.log(previousOption);
        // console.log(startPosition, endPosition);
        const navbarBg = this.$refs.navbarBg;
        // console.log(navbarBg);
        // Animando el icono de salida
        const bgAnimation = navbarBg.animate([
            { transform : `translateX(${startPosition}px)` },
            {
              transform : `translateX(${endPosition}px)`,
              backgroundPositionX: `${backgroundPosBase}%`
            }
          ],
          {
            duration: 500,
            fill: 'forwards',
            easing: 'ease'
          }
        );

        bgAnimation.onfinish = () => {
          // console.log('se finalizo');
          target.classList.add('hide');
          // console.log('agregando la clase hide a :');
          // console.log(target);
        };
      }, 300);

      setTimeout(() => {
        console.log(this, option.icon);
        this.currentIcon = option.icon;
        console.log(this.currentIcon);
      }, 500);

      setTimeout(() => {
        // const circleIcon = this.$refs.navbarCircle.querySelector('path');      
        // // Animando el icono de salida
        // circleIcon.animate(
        //   [
        //     { 
        //       fill: '#ffffff',
        //       strokeDashoffset: '2000',
        //       // opacity: 0
        //     },
        //     { 
        //       fill: '#000000',
        //       strokeDashoffset: '0',
        //       // opacity: 1
        //     }
        //   ],
        //   {
        //     duration: 3000,
        //     fill: 'forwards'
        //   }
        // );

        const circleSvg = this.$refs.navbarCircle.querySelector('path').parentNode;   
          // Animando el icono de salida
          circleSvg.animate(
            [
              {
                strokeDashoffset: '2000'
                // opacity: '0',
                // transform: 'translateY(30px)'
              },
              {
                strokeDashoffset: '0'
                // opacity: '1',
                // transform: 'translateY(0px)'
              }
            ],
            {
              duration: 800,
              fill: 'forwards',
              easing: 'ease'
            }
          );
      }, 500);


      this.previousOptionIndex = index;

    },
    getSizeCircle(){
      return this.$refs.navbarCircle.getBoundingClientRect().width;
    },
    getSizeBg(){
      return this.$refs.navbarBg.getBoundingClientRect().width;
    }
  },
  mounted(){
    // calculamos el centro de el navbar
    const navbarCenter = window.screen.availWidth / 2;
    document.querySelector('a[data-in="2"]').classList.add('hide');;
    
    // Movemos el circulo al centro
    this.$refs.navbarCircle.style.left = + ((this.getSizeBg() - this.getSizeCircle()) / 2) + 'px';
    this.$refs.navbarCircle.style.top = + ((this.getSizeBg() - this.getSizeCircle()) / 2) + 'px';
    this.$refs.navbarBg.style.left = (navbarCenter - (this.getSizeBg() / 2)) + 'px';
    this.$refs.navbarBg.style.backgroundSize = `${window.screen.availWidth}px ${window.screen.availHeight}px`;
    this.$refs.navbarBg.classList.add('navbar-menu2__bg--show');
  }
}

</script>