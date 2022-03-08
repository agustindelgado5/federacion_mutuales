<template>
  <div>
    <b-table
      :fields="fields"
      :items="items"
      small
      hover
      striped
      sortable
      show-empty
      responsive
      selectable
      ref="tablaregistros"
      id="tablaregistros"
      class="myTable"
    >
      <template #empty>
        <b>No hay registros para mostrar</b>
      </template>
      <template slot="cell(action)" slot-scope="row">
        <div class="mt-3">
          <b-button-group>
            <b-button variant="warning" title="Editar este registro" @click="selectRow(row)"
              ><v-icon class="mr-2"> mdi-pencil </v-icon> Editar</b-button
            >
            <b-button
              variant="danger"
              title="Eliminar este registro"
              @click="deleteItem(row)"
            >
              <v-icon class="mr-2"> mdi-delete </v-icon>
              Eliminar</b-button
            >
          </b-button-group>
        </div>
      </template>
    </b-table>
    <b-modal id="modal-delete" title="Eliminar" ok-only>
        <p class="my-4">Hello from modal!</p>
    </b-modal>
  </div>
</template>

<script>
export default {
  props: ["fields", "items", "deleteFunction", "selectRow"],
  methods: {
    async deleteItem(row) {
      if (confirm("Seguro quiere eliminar?")) {
        this.deleteFunction(row)
      }
    },
  },
};
</script>

<style scoped>
.myTable {
		position: absolute;
		left: 0;
		padding: 1.5em;
		margin-top: 4rem;
		overflow: auto;
		transition: 0.5s;
		width: 100%;
	}
</style>