<template>
  <div>
    <h1>HI, WELCOME TO TEST VIEW</h1>
    <BaseForm :fields="fields"/>
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
          id: "field_id",
          value: "holius",
          type: "text",
          label: "field_label",
          placeholder: "field_placeholder",
          invalid_feedback: "field_invaild",
          required: true,
          options: [1, 2, 3, 4, 5],
        },
        {
          form_input: "select",
          id: "field_id",
          value: "holius",
          type: "text",
          label: "field_label",
          placeholder: "field_placeholder",
          invalid_feedback: "field_invaild",
          required: true,
          options: [1, 2, 3, 4, 5],
        },
        {
          form_input: "textarea",
          id: "field_id",
          value: "holius",
          type: "text",
          label: "field_label",
          placeholder: "field_placeholder",
          invalid_feedback: "field_invaild",
          required: true,
        },
        {
          form_input: "input",
          id: "field_id",
          value: "holius",
          type: "date",
          label: "field_label",
          placeholder: "field_placeholder",
          invalid_feedback: "field_invaild",
          required: true,
          options: [1, 2, 3, 4, 5],
        },
      ],
    };
  },
};
</script>

<style>
</style>