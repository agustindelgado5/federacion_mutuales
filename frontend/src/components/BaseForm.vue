<template>
  <div>
    <b-card class="border-0" :title="title">
      <h6>Los campos en (*) son obligatorios</h6>
      <b-form>
        <div v-for="(field, index) in fields" :key="index">
          <b-form-group
            :id="field.id"
            :label="field.label"
            :label-for="field.id"
          >
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
        <b-button
          type="submit"
          class="mt-2"
          variant="success"
          block
          @click.prevent="processForm()"
          >Guardar</b-button
        >
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  props: ["fields", "title", "createFunction", "updateFunction"],
  data() {
    return {
      payload: {},
    };
  },
  methods: {
    async processForm() {
      let formInput = {};
      this.fields.forEach((field) => {
        formInput[field.name] = field.value;
      });
      if (this.createFunction) await this.createFunction(formInput);
      else await this.updateFunction(formInput);
    },
  },
};
</script>

<style>
</style>