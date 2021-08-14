<template>
  <div class="navbar-menu__wrapper">
    <div class="navbar-menu">
      <div class="navbar-menu__circle">
        <div class="circle" ref="navbarCircle"></div>
      </div>
      <div 
        class="navbar-menu__item"
        v-for="(option, index) in options"
        :key="'op' + index"
        @click="setCurrentOption(index)"
      >
        <div class="navbar-menu__icon">
          
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  
export default {
  name: 'NavbarMenu',
  data(){
    return {
      options: [
        {
          icon: '1',
          link: '1'
        },
        {
          icon: '2',
          link: '2',
          default: true
        },
        {
          icon: '3',
          link: '3'
        }
      ],
      origins: [],
      screenWidth: 0,
      xCircleInit: 0,
      yCircleInit: 0,
      xCircle: 0,
      yCircle: 0,
      sizeCircle: 0,
      navbarHeight: 40,
      transitionDuration: 300,
      transitions: [],
      currentOptionIndex: 1,
      prevOptionIndex: null,
      nextOptionIndex: null
    }
  },
  methods: {
    setDefaultOption(){
      console.log('default');
      for (let i = 0; i < this.options.length; i++) {
        if(this.options[i].default){
          const x = (this.screenWidth * i / this.options.length) + this.xCircleInit;
          const y = (this.navbarHeight - this.sizeCircle) / 2;
          this.setCirclePosition(x, y);
          const origin = this.origins[i];
          this.origins[i] = {...this.origins[i], selected: true};
          this.setCircleTransformOrigin(origin.x, origin.y);
        }
      }
    },
    setCirclePosition(x, y){
      console.log(`updating circle position to x:${x} ; y:${y}`);
      this.$refs.navbarCircle.style.left = `${x}px`;
      this.$refs.navbarCircle.style.top = `${y}px`;

      // this.xCircle = `${x}px`;
      // this.yCircle= `${y}px`;
    },
    setCircleTransformOrigin(x, y){
      console.log(`updating circle transform origin to x:${x} ; y:${y}`);
      this.$refs.navbarCircle.parentNode.style.transformOrigin = `${x}px ${y}px`;
    },
    setCurrentOption(i){
      console.log('Hay que cambiar a la posicion ' + i);
      const steps = i - this.currentOptionIndex;
      console.log('hay que dar pasos: ' + steps);
      this.nextOptionIndex = steps > 0 ? this.currentOptionIndex + 1 : this.currentOptionIndex - 1;
      console.log('El siguinte index es: ' + this.nextOptionIndex);
      console.log('El indice actual es: ' + this.currentOptionIndex);
      this.targetIndex = i;
      console.log('El nuevo index es: ' + this.targetIndex);

      this.changeOption(steps);
    },
    rotateCircle(deg){
      console.log(`roting circle${deg} grados `);
      this.$refs.navbarCircle.parentNode.style.transform = `rotate(${deg}deg)`;
    },
    changeOption(steps){
      let nextIndex = this.nextOptionIndex;
      let currentIndex = this.currentOptionIndex;
      for (let i = 0; i < Math.abs(steps); i++) {
        let transition = {};
        if (steps > 0) {
          transition.origin = this.origins[nextIndex - 1];
          transition.rotate = nextIndex === 1 ? 0 : 115;
          nextIndex += 1;
        } else if(steps < 0){
          transition.origin = this.origins[nextIndex];
          transition.rotate = nextIndex === 1 ? 0 : -115;
          nextIndex -= 1;
        }
        this.transitions.push(transition);
      }
      this.currentOptionIndex = this.targetIndex;
      console.log(this.transitions);
      this.runTransitions();
    },
    runTransitions(){
      this.transitions.forEach((transition, index) => {
        const time = index * this.transitionDuration;
        console.log(this.transitions);
        setTimeout(() => {
          console.log('ejecutando la transicion ' + index);
          this.setCircleTransformOrigin(transition.origin.x, transition.origin.y);
          this.rotateCircle(transition.rotate);
          console.log('termino de ejecutar la ' + index);
        }, time);
      });
      this.transitions = [];
    },
    calculateOptionsPosition(){
      this.options.forEach((option, index) => {
        option.x = ((this.screenWidth / this.options.length) * index) + this.xCircleInit;
        option.y = this.yCircleInit;
        if(option.default) option.selected = true;
      });
    },
    calculateOrigins(){
      const widthItems = this.screenWidth / this.options.length;
      for(let i = 1; i < this.options.length; i++){
        const x = widthItems * i;
        const y = 58
        this.origins.push({ x, y});
      }
    }


  },
  mounted(){
    this.screenWidth = window.screen.width;
    this.sizeCircle = 25;
    this.xCircleInit = (this.screenWidth / (this.options.length * 2)) - (this.sizeCircle / 2);
    this.yCircleInit = (this.navbarHeight - this.sizeCircle) / 2;
    this.calculateOrigins();
    this.setDefaultOption();
    this.calculateOptionsPosition();
  }
}

</script>