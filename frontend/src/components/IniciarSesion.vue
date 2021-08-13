<template>
    <div>
        <img src="../assets/logo_fed.jpg" alt="Logo Federación" srcset="" id="Logo">
        <b-card bg-variant="light">
            
            <b-form-group
                label-cols-lg="3"
                label="INICIAR SESION"
                label-size="lg"
                label-class="font-weight-bold pt-0"
                class="mb-0"
            >   
                

                <b-form-group
                label="DNI TITULAR:"
                label-for="dni"
                label-cols-sm="3"
                label-align-sm="right"
                 >
                    <b-form-input id="user"></b-form-input>
                </b-form-group>
                <b-form-group
                label="CONTRASEÑA:"
                label-for="password"
                label-cols-sm="3"
                label-align-sm="right"
        
                >
                    <b-form-input id="password" type="password"></b-form-input>
                </b-form-group>
            </b-form-group>
        </b-card>
    </div>
</template>

<script>
export default {

}
</script>

<style>
#Logo {
  width: 15%;
  float: left;
  margin: 0.625em;
  /*display: block;*/
  /*margin: auto;*/
}
</style>