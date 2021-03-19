import { createStore } from 'vuex'

const state = {
    prediction: {
        willClick: false,
        probability: 0
    }
}

const mutations = {
    setPrediction(state, prediction) {
        state.prediction = prediction
    }
}


export default createStore({ state, mutations })