<template>
  <div>
    <Prediction />

    <p>Will click: {{ prediction.willClick}} </p>
    <p>Probability: {{ prediction.probability }} </p>
    
  </div>
  
</template>

<script>
import Prediction from './components/Prediction.vue'

export default {
  name: 'App',
  components: {
    Prediction
    
  }, 
  computed: {
    prediction() {
      return this.$store.state.prediction
    }
  }
}
</script>

