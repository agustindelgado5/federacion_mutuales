<template>
  <div>
    <BaseForm :fields="fields" title="Alta servicio" />
  </div>
</template>

<script>
import BaseForm from "../../components/BaseForm.vue";
export default {
  components: { BaseForm },
  data() {
    return {
      fields: [
        {
          form_input: "input",
          id: "servicio",
          name: "servicio",
          value: "",
          type: "text",
          label: "Servicio",
          placeholder: "Ej: Odontología",
          invalid_feedback: "Ingrese un nombre de servicio valido",
          required: true,
        },
      ],
    };
  },
};
</script>

<style>
</style>