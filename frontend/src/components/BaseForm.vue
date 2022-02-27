<template>
  <div>
    <b-form>
      <div v-for="(field, index) in fields" :key="index">
        <b-form-group :id="field.id" :label="field.label" :label-for="field.id">
          <div v-if="field.form_input === 'input'">
            <b-form-input
              :id="field.id"
              :type="field.type"
              :placeholder="field.placeholder"
              :required="field.required"
              :invalid-feedback="field.invalid_feedback"
              v-model="field.value"
            >
            </b-form-input>
          </div>
          <div v-else-if="field.form_input === 'select'">
            <b-form-select
              :id="field.id"
              :type="field.type"
              :placeholder="field.placeholder"
              :required="field.required"
              :invalid-feedback="field.invalid_feedback"
              :options="field.options"
              v-model="field.value"
            >
            </b-form-select>
          </div>
          <div v-else-if="field.form_input === 'textarea'">
            <b-form-textarea
              :id="field.id"
              :type="field.type"
              :placeholder="field.placeholder"
              :required="field.required"
              :invalid-feedback="field.invalid_feedback"
              v-model="field.value"
              rows="3"
              max-rows="6"
            >
            </b-form-textarea>
          </div>
        </b-form-group>
      </div>
      <b-button type="submit" variant="primary">Guardar</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  props: [
      'fields',
  ],
  data() {
    return {
    };
  },
};
</script>

<style>
</style>