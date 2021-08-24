<template>
    <div class="d-block text-center">
        <h3>¿Esta seguro de eliminar los datos de ... ?</h3>
    </div>
    <!--
    <b-button
    class="mt-2"
    block
    @click="hideModal"
    title="Volver Atras"
    >
        <v-icon
        dark
        left
        >
            mdi-arrow-left
        </v-icon>
        Volver Atras
  </b-button>
  <b-button
    class="mt-3"
    variant="danger"
    block
    title="Eliminar"
  >
    Eliminar
  </b-button>
  -->
</template>

<script>
export default {
    data() {
        return {
            list_socios:{},
            data: {},
        }
    },

    methods: {
        async getSocios() {
            let socioAPI = new APIControler();
            socioAPI.apiUrl.pathname='socios/';
            this.data = await socioAPI.getData(this.list_socios) 
        },
        async deleteSocio(){},

        //Funcion para mostrar el modal
        showModal() {
            this.$refs["my-modal"].show();
        },
        //Funcion para esconder el modal
        hideModal() {
            this.$refs["my-modal"].hide();
        },

    }
}
</script>