<template>
	<v-app id="app">
		<div id="ordenes" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Ordenes - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Ordenes</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA ORDENES======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaOrden()"
				title="Nueva Orden"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nueva Orden
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<ordenes-alta :updateTable="testFetch" />
			</b-modal>

			<!-- ================ELIMINAR VARIAS ORDENES======================== -->
			<b-button
				class="mb-4 ml-2"
				variant="danger"
				id="btn_del_full"
				title="Eliminar todos los registros"
				style="color: white"
				:disabled="btn_del_full"
				v-b-modal.modal-eliminarTodo
			>
				<v-icon class="mr-2" style="color: white"> mdi-delete </v-icon>
				Eliminar
			</b-button>

			<div>
				<b-modal
					ref="my-modal"
					id="modal-eliminarTodo"
					hide-footer
					title="Eliminar"
					ok-only
				>
					<div class="d-block text-center" v-if="selected.length === rows">
						<h3>¿Esta seguro de eliminar todos los registros ?</h3>
					</div>
					<div class="d-block text-center" v-else>
						<h3>¿Esta seguro de eliminar {{ selected.length }} registros ?</h3>
					</div>

					<b-button class="mt-2" block @click="hideModal" title="Volver Atras">
						Volver Atras
					</b-button>

					<b-button
						class="mt-3"
						variant="danger"
						block
						title="Eliminar"
						@click="delete_all_Ordenes()"
					>
						Eliminar
					</b-button>
				</b-modal>
			</div>

			<!-- ======== Formulario de Busqueda ======== -->
			<b-form-group
				label-for="filter-input"
				label-align-sm="right"
				label-size="sm"
				class="mb-0"
				style="width: 100%; padding-bottom: 1em"
				v-show="rows > 0"
			>
				<b-input-group size="sm">
					<b-form-input
						id="filter-input"
						v-model="filter"
						type="search"
						placeholder="Buscar registros"
					></b-form-input>

					<b-input-group-append>
						<b-button :disabled="!filter" @click="filter = ''"
							>Limpiar</b-button
						>
					</b-input-group-append>
				</b-input-group>
			</b-form-group>
			<!-- ======================================== -->

			<!-- ======================================== -->

			<div v-if="rows > 0">
				<div v-if="selected.length > 0">
					<div v-if="rows != rowsFilter">
						<pre>
Registros Fitrados: {{ rowsFilter }} | Filas seleccionadas: {{
								selected.length
							}}</pre
						>
					</div>
					<div v-else>
						<pre>
Cantidad de registros: {{ rows }} | Filas seleccionadas: {{
								selected.length
							}}</pre
						>
					</div>
				</div>
				<div v-else>
					<div v-if="rows != rowsFilter">
						<pre>Registros Fitrados: {{ rowsFilter }} </pre>
					</div>
					<div v-else>
						<pre>Cantidad de registros: {{ rows }}</pre>
					</div>
				</div>
				<b-button
					class="mb-4 ml-2"
					size="sm"
					style="color: white"
					title="Seleccionar Todo"
					@click="seleccionar_todas"
					:disabled="btn_select"
				>
					Seleccionar Todo
				</b-button>
				<b-button
					class="mb-4 ml-2"
					size="sm"
					style="color: white"
					title="Limpiar Seleccion"
					@click="limpiar_seleccion"
					:disabled="btn_limpiar"
				>
					Limpiar Seleccion
				</b-button>
			</div>
			<div v-else>
				<pre>Cantidad de registros: {{ rows }}</pre>
			</div>

			<section class="container">
				<!-- ======== Tabla con los registros ======= -->

				<b-table
					:fields="fields"
					striped
					sortable
					responsive
					hover
					:items="
						tabla_ordenes
							| FechaRange(filter_fecha.desde, filter_fecha.hasta)
							| Servicio(filter_servicio)
							| Realizado(filter_realizado)
							| Presentada(filter_presentada)
							| Vencida(filter_vencida)
							| MutualesOrden(filter_mutual)
					"
					show-empty
					:per-page="perPage"
					:current-page="currentPage"
					:sticky-header="true"
					:no-border-collapse="false"
					ref="tablaregistros"
					id="tablaregistros"
					:filter="filter"
					@filtered="onFiltered"
					@row-selected="seleccionar_una"
					selectable
					select-mode="multi"
				>
					<template #empty="">
						<b>No hay registros para mostrar</b>
					</template>

					<template #cell(selected)="{ rowSelected }">
						<template v-if="rowSelected">
							<span aria-hidden="true">&check;</span>
							<span class="sr-only">Selected</span>
						</template>
						<template v-else>
							<span aria-hidden="true">&nbsp;</span>
							<span class="sr-only">Not selected</span>
						</template>
					</template>

					<template slot="cell(numero_orden)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>
					<template slot="cell(socio)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>
					<template slot="cell(paciente)" slot-scope="data">
						{{ data.value.split("/")[4] }}
					</template>
					<template slot="cell(medico)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>
					<template slot="cell(mutual)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>
					<template slot="cell(fecha)" slot-scope="data">
						{{ data.value | Date }}
					</template>
					<template slot="cell(hora)" slot-scope="data">
						{{ data.value | FormatStringToTime }}
					</template>

					<template slot="cell(preciosocio)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>
					<template slot="cell(preciomutual)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>

					<template slot="cell(realizado)" slot-scope="data">
						<div v-if="data.value === true">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-check-circle-fill"
								viewBox="0 0 16 16"
								style="color: green"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
								/>
							</svg>
							SI
						</div>
						<div v-else>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-x-circle-fill"
								viewBox="0 0 16 16"
								style="color: red"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"
								/>
							</svg>
							NO
						</div>
					</template>
					<template slot="cell(presentada)" slot-scope="data">
						<div v-if="data.value === true">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-check-circle-fill"
								viewBox="0 0 16 16"
								style="color: green"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
								/>
							</svg>
							SI
						</div>
						<div v-else>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-x-circle-fill"
								viewBox="0 0 16 16"
								style="color: red"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"
								/>
							</svg>
							NO
						</div>
					</template>
					<template slot="cell(vencida)" slot-scope="data">
						<div v-if="data.value === true">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-check-circle-fill"
								viewBox="0 0 16 16"
								style="color: green"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
								/>
							</svg>
							SI
						</div>
						<div v-else>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-x-circle-fill"
								viewBox="0 0 16 16"
								style="color: red"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"
								/>
							</svg>
							NO
						</div>
					</template>
					<template slot="cell(action)" slot-scope="row">
						<div class="mt-3">
							<b-button-group>
								<!-- ==================================CREAR PDF================================== -->
								<!-- Generar PDF -->
								<b-button
									@click="generarPDF(row.item)"
									id="btn_down_pdf"
									class="mb-0 ml-2"
									title="Generar PDF"
									variant="info"
									style="color: white"
									:disabled="btn_down_pdf"
								>
									<!-- :disabled="btn_down_pdf" -->
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="16"
										height="16"
										fill="currentColor"
										class="bi bi-file-pdf-fill"
										viewBox="0 0 16 16"
									>
										<path
											d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z"
										/>
										<path
											fill-rule="evenodd"
											d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z"
										/>
									</svg>
									Generar
									<!-- ============================================================================== -->
								</b-button>
								<b-button
									variant="warning"
									id="button-2"
									title="Editar este registro"
									v-b-modal.modal-editar
									@click="editarOrden(row.item, row.index)"
									:disabled="btn_editar"
								>
									<v-icon class="mr-2"> mdi-pencil </v-icon>
									Editar
								</b-button>

								<b-button
									variant="danger"
									id="button-3"
									@click="showModalinfo(row.item, row.index)"
									title="Eliminar este registro"
									:disabled="btn_eliminar"
								>
									<v-icon class="mr-2"> mdi-delete </v-icon>
									Eliminar
								</b-button>
							</b-button-group>
						</div>
					</template>
				</b-table>

				<b-container fluid>
					<b-col class="my-1">
						<b-pagination
							v-model="currentPage"
							align="center"
							pills
							:total-rows="totalRows"
							:per-page="perPage"
							aria-controls="table_ordenes"
						>
						</b-pagination>
					</b-col>
				</b-container>
			</section>

			<aside v-show="rows > 0">
				<div>
					<b-card-group deck>
						<b-card
							bg-variant="primary"
							text-variant="white"
							header="REGISTROS POR PAGINA"
							class="text-center"
						>
							<b-form-group label-for="per-page-select" class="mb-0">
								<b-form-select
									id="per-page-select"
									v-model="perPage"
									:options="pageOptions"
									size="sm"
								></b-form-select>
							</b-form-group>
						</b-card>
					</b-card-group>
				</div>

				<br />

				<div>
					<b-card-group deck>
						<b-card
							bg-variant="primary"
							text-variant="white"
							header="FILTRAR POR"
							class="text-center"
						>
							<div class="accordion" role="tablist">
								<b-card no-body>
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-1
											variant="info"
											style="font-size: 0.82em"
										>
											REALIZADA
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-1"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group
												id="input-group-4"
												v-slot="{ ariaDescribedby }"
											>
												<b-form-checkbox-group
													v-model="filter_realizado"
													id="orden_pagada"
													:aria-describedby="ariaDescribedby"
													style="color: black"
												>
													<b-form-checkbox value="1">NO❌</b-form-checkbox>
													<b-form-checkbox value="0">SI✔️</b-form-checkbox>
												</b-form-checkbox-group>
												<br />
												<div v-show="filter_realizado != null">
													<b-button
														@click="filter_realizado = null"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>

									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-2
											variant="info"
											style="font-size: 0.82em"
										>
											PRESENTADA
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-2"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group
												id="input-group-4"
												v-slot="{ ariaDescribedby }"
											>
												<b-form-checkbox-group
													v-model="filter_presentada"
													id="orden_pagada"
													:aria-describedby="ariaDescribedby"
													style="color: black"
												>
													<b-form-checkbox value="1">NO❌</b-form-checkbox>
													<b-form-checkbox value="0">SI✔️</b-form-checkbox>
												</b-form-checkbox-group>
												<br />
												<div v-show="filter_presentada != null">
													<b-button
														@click="filter_presentada = null"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>

									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-3
											variant="info"
											style="font-size: 0.82em"
										>
											VENCIDA
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-3"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group
												id="input-group-4"
												v-slot="{ ariaDescribedby }"
											>
												<b-form-checkbox-group
													v-model="filter_vencida"
													id="orden_pagada"
													:aria-describedby="ariaDescribedby"
													style="color: black"
												>
													<b-form-checkbox value="1">NO❌</b-form-checkbox>
													<b-form-checkbox value="0">SI✔️</b-form-checkbox>
												</b-form-checkbox-group>
												<br />
												<div v-show="filter_vencida != null">
													<b-button
														@click="filter_vencida = null"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>

									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-4
											variant="info"
											style="font-size: 0.82em"
										>
											SERVICIO
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-4"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<v-autocomplete
													id="servicio"
													v-model="filter_servicio"
													:items="options_servicio"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_servicio != null">
													<b-button
														@click="filter_servicio = null"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-5
											variant="info"
											style="font-size: 0.82em"
										>
											FECHA
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-5"
										visible
										accordion="my-accordion"
										role="tabpanel"
										style="color: black"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<b-form-group label="Desde" label-for="fecha_desde">
													<b-form-input
														id="fecha_desde"
														v-model="filter_fecha.desde"
														type="date"
													></b-form-input>
												</b-form-group>
												<b-form-group label="Hasta" label-for="fecha_hasta">
													<b-form-input
														id="fecha_inicio_hasta"
														v-model="filter_fecha.hasta"
														type="date"
													></b-form-input>
												</b-form-group>

												<div style="color: black">
													{{ filter_fecha.desde }} <br />
													{{ filter_fecha.hasta }} <br />
												</div>
												<div
													v-show="
														filter_fecha.desde != null &&
														filter_fecha.hasta != null
													"
												>
													<b-button
														@click="limpiar_filtro_fecha()"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>

									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-6
											variant="info"
											style="font-size: 0.82em"
										>
											MUTUAL
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-6"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group id="input-group-7">
												<v-autocomplete
													id="mutual"
													v-model="filter_mutual"
													:items="options_mutual"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_mutual != null">
													<b-button
														@click="filter_mutual = null"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>
								</b-card>
							</div>
						</b-card>
					</b-card-group>
				</div>
			</aside>

			<!-- ================ELIMINAR ORDEN======================== -->

			<b-modal
				id="modal_eliminar"
				ref="my-modal"
				hide-footer
				title="Eliminar"
				ok-only
			>
				<div class="d-block text-center">
					<h3>
						¿Esta seguro de eliminar los datos de la orden
						{{ infoEliminar.orden.numero_orden }}?
					</h3>
				</div>
				<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
					>Volver Atras</b-button
				>
				<b-button
					class="mt-3"
					variant="danger"
					block
					@click="deleteOrden(infoEliminar.orden.numero_orden)"
					title="Eliminar"
				>
					Eliminar
				</b-button>
			</b-modal>
			<!-- ================EDITAR ORDEN======================== -->
			<b-modal id="modal-editar" hide-footer>
				<template #modal-title><h5 class="modal-title">Editar</h5></template>
				<ordenes-update :orden="editar" :updateTable="testFetch" />
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<vue-html2pdf
				:show-layout="false"
				:float-layout="true"
				:enable-download="false"
				:preview-modal="true"
				:paginate-elements-by-height="1400"
				filename="DetalleOrden"
				:pdf-quality="2"
				:manual-pagination="false"
				pdf-format="a4"
				pdf-orientation="portrait"
				pdf-content-width="80%"
				@progress="onProgress($event)"
				@startPagination="startPagination()"
				@hasPaginated="hasPaginated()"
				@beforeDownload="beforeDownload($event)"
				@hasDownloaded="hasDownloaded($event)"
				ref="html2Pdf"
			>
				<section slot="pdf-content">
					<!-- PDF Content Here -->
					<section class="pdf-item">
						<h3>Federación Tucumana de Mutuales</h3>
						<img
							src="@/assets/logo.jpg"
							alt="Logo Federación"
							srcset=""
							id="Logo_fed"
						/>
					</section>
					<section class="pdf-item">
						<h3>Orden Médica</h3>

						<b-list-group>
							<b-list-group-item
								v-for="value in fields.slice(0, -1)"
								:key="value.key"
								>{{ value.label }}:
								{{ ordenAPDF[value.key] }}</b-list-group-item
							>
						</b-list-group>
					</section>
				</section>
			</vue-html2pdf>
			<!-- ============================================================================== -->
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "ordenes";
	//api.port = 8000;
	api.port = 8081;
	import { APIControler } from "@/store/APIControler";
	import OrdenesAlta from "./OrdenesAlta.vue";
	import OrdenesUpdate from "./OrdenesUpdate.vue";
	import VueHtml2pdf from "vue-html2pdf";

    import _ from "lodash";
    import axios from "axios";
    import { mapState, mapActions } from "vuex";

	export default {
		components: { OrdenesAlta, OrdenesUpdate, VueHtml2pdf },
		data() {
			return {
				tabla_ordenes: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "numero_orden", label: "N° Orden", sortable: true },
					{ key: "socio", label: "N° Socio", sortable: true },
					{ key: "paciente", label: "Paciente", sortable: true },
					{ key: "servicio", label: "Servicio", sortable: true },
					{ key: "medico", label: "Id Medico", sortable: true },
					{ key: "mutual", label: "Id Mutual", sortable: true },
					{ key: "fecha", label: "Fecha", sortable: true },
					{ key: "hora", label: "Hora", sortable: true },
					{ key: "preciosocio", label: "Precio Socio", sortable: true },
					{ key: "preciomutual", label: "Precio Mutual", sortable: true },
					{ key: "realizado", label: "Realizado", sortable: true },
					{ key: "presentada", label: "Presentada", sortable: true },
					{ key: "vencida", label: "Vencida", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				filter: null,
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				buscar: "",
				editar: {},
				infoEliminar: {
					id: "modal_eliminar",
					orden: -1,
				},
				selected: [],

				//Botones
				btn_down_pdf: false, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_limpiar: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_ordenes: false,
				btn_eliminar: false,
				btn_select: false,

				//Campos a filtrar
				filter_fecha: {
					desde: null,
					hasta: null,
				},
				filter_servicio: null,
				filter_realizado: null,
				filter_vencida: null,
				filter_presentada: null,
				filter_socio: null,
				filter_paciente: null,
				filter_medico: null,
				filter_mutual: null,

				//Opciones de filtrado
				options_mutual: [
					{ value: null, text: "Elija un mutual", selected: true },
				],

				options_servicio: [{ value: null, text: "Elija un servicio" }],
				ordenAPDF: {}, //Se carga cuando se hace clic en exportar a pdf, con la orden a exportar
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_ordenes.length);
			},
			rowsFilter() {
				return this.totalRows;
			},

			sortOptions() {
				// Create an options list from our fields
				return this.fields
					.filter((f) => f.sortable)
					.map((f) => {
						return { text: f.label, value: f.key };
					});
			},
		},
		methods: {
			async testFetch() {
				try {
					const res = await fetch(api);
					const data = await res.json();

					var lista_ordenes = data.results;

					console.log(lista_ordenes);

					//this.tabla_ordenes = lista_ordenes;
					this.tabla_ordenes = await this.getMutual(lista_ordenes);
					this.getSocio();

					this.tabla_ordenes.forEach((element) => {
						//let opcionSoc = {};
						let opcion = {};
						let opcionMut = {};

						opcion.value = element.servicio;
						opcion.text = element.servicio;

						opcionMut.value = element.mutual;
						opcionMut.text = element.mutual;
						if (this.options_servicio.find((x) => x.value == opcion.value)) {
							console.log(opcion, " ya se encuentra en el listado");
						} else {
							this.options_servicio.push(opcion);
						}

						if (this.options_mutual.find((x) => x.value == opcionMut.value)) {
							console.log(opcionMut, " ya se encuentra en el listado");
						} else {
							this.options_mutual.push(opcionMut);
						}
					});
				} catch (error) {
					console.log(error);
				}
			},

			async getMutual(lista_ordenes) {
				let listado = {};
				let DataReturn = [];
				let mutualAPI = new APIControler();
				mutualAPI.apiUrl.pathname = "mutuales/";
				let mutuales = await mutualAPI.getData(listado);
				console.log("DATA LAS MUTUALES: ", mutuales);

				mutuales.forEach((element) => {
					var idMut =
						"http://localhost:8081/mutuales/" + element.id_mutual + "/";
					lista_ordenes.forEach((orden) => {
						if (idMut == orden.id_mutual) {
							let datos = {};
							datos.numero_orden = orden.numero_orden;
							datos.socio = orden.numero_socio;
							datos.paciente = orden.paciente;
							datos.medico = orden.id_medico;
							datos.servicio = orden.servicio;
							datos.mutual = element.id_mutual + "- " + element.nombre;
							datos.fecha = orden.fecha;
							datos.hora = orden.hora;
							datos.fecha_presentacion = orden.fecha_presentacion;
							datos.preciosocio = orden.preciosocio;
							datos.preciomutual = orden.preciomutual;
							datos.presentada = orden.presentada;
							datos.realizado = orden.realizado;
							datos.vencida = orden.vencida;
							DataReturn.push(datos);
						}
					});
				});
				return DataReturn;
			},

			async getSocio() {
				let listado = {};
				//let DataReturn = [];
				let socioAPI = new APIControler();
				socioAPI.apiUrl.pathname = "socios/";
				let socios = await socioAPI.getData(listado);
				console.log("DATA LOS SOCIOS: ", socios);

				socios.forEach((element) => {
					var IdSocio =
						"http://localhost:8081/socios/" + element.numero_socio + "/";
					this.tabla_ordenes.forEach((orden) => {
						if (IdSocio == orden.socio) {
							orden.socio =
								element.numero_socio +
								"- " +
								element.apellido +
								", " +
								element.nombre;
						}
					});
				});
				this.getProfesional();
				//return DataReturn;
			},

			async getProfesional() {
				let listado = {};
				let profesionalAPI = new APIControler();
				profesionalAPI.apiUrl.pathname = "profesionales/";
				let profesionales = await profesionalAPI.getData(listado);
				console.log("DATA LOS PROFESIONALES: ", profesionales);

				profesionales.forEach((element) => {
					var IdMed =
						"http://localhost:8081/profesionales/" + element.id_medico + "/";
					this.tabla_ordenes.forEach((orden) => {
						if (IdMed == orden.medico) {
							orden.medico =
								element.id_medico +
								"- " +
								element.apellido +
								", " +
								element.nombre;
						}
					});
				});
				//return DataReturn;
			},
			editarOrden(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.orden = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaOrden() {},

			//Elimino una orden
			async deleteOrden(nro_orden) {
				axios
					.delete("http://localhost:8081/ordenes/" + nro_orden + "/")
					.then((datos) => {
						swal("Operación Exitosa", " ", "success");
						console.log(datos);
						this.hideModal();
                        sessionStorage.removeItem("pagos");
					})
					.catch((error) => {
						swal("¡ERROR!", "Se ha detectado un problema ", "error");
						console.log(error);
						this.hideModal();
					})
					.finally(() => this.testFetch());
			},

			//Funcion para eliminar todos los profesionales
			async delete_all_Ordenes() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/ordenes/" +
								this.selected[i].numero_orden +
								"/"
						);
                        sessionStorage.removeItem("pagos");
						if (this.selected.length == 0) {
							console.log("Eliminacion Exitosa");
							break;
						}
					}
					this.hideModal();
					swal("Eliminacion Exitosa", " ", "success");
				} catch (error) {
					this.hideModal();
					swal("¡ERROR!", "Se ha detectado un problema ", "error");
					console.log(error);
				} finally {
					this.testFetch();
				}
			},

			//Selecciona una a una
			seleccionar_una(items) {
				this.selected = items;
				if (this.selected.length > 0) {
					this.btn_del_full = false;
					this.btn_limpiar = false;
					if (this.selected.length > 1) {
						this.btn_mostrar = true;
						this.btn_editar = true;
						this.btn_eliminar = true;
						this.btn_down_pdf = true;
					}
					if (this.selected.length == this.rows) {
						this.btn_select = true;
					} else {
						this.btn_select = false;
					}
				} else {
					this.btn_del_full = true;
					this.btn_mostrar = false;
					this.btn_editar = false;
					this.btn_eliminar = false;
					this.btn_limpiar = true;
					this.btn_down_pdf = false;
				}
			},
			//Selecciona todas
			seleccionar_todas() {
				this.$refs.tablaregistros.selectAllRows();
				this.btn_del_full = false;
				this.btn_mostrar = true;
				this.btn_editar = true;
				this.btn_eliminar = true;
				this.btn_down_pdf = true;

				this.btn_select = true;
				this.btn_limpiar = false;
			},
			//Limpia todas las selecciones
			limpiar_seleccion() {
				this.$refs.tablaregistros.clearSelected();
				this.btn_del_full = true;
				this.btn_mostrar = false;
				this.btn_editar = false;
				this.btn_eliminar = false;
				this.btn_down_pdf = false;

				this.btn_select = false;
				this.btn_limpiar = true;
			},
			//Funcion de busqueda
			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
			},
			//Funcion para crear el PDF
			async generarPDF(item) {
				//let resultMed = (await axios.get(item.id_medico)).data;
				//let resultMutual = (await axios.get(item.id_mutual)).data;
				//let resultSocio = (await axios.get(item.numero_socio)).data;
				let resultPaciente = (await axios.get(item.paciente)).data;

				this.ordenAPDF = { ...item };
				this.ordenAPDF.realizado = item.realizado ? "Si" : "No";
				this.ordenAPDF.presentada = item.presentada ? "Si" : "No";
				this.ordenAPDF.vencida = item.vencida ? "Si" : "No";
				//this.ordenAPDF.id_medico = resultMed.apellido + ", " + resultMed.nombre;
				//this.ordenAPDF.id_mutual = resultMutual.nombre;
				//this.ordenAPDF.numero_socio = resultSocio.apellido + ", " + resultSocio.nombre;
				this.ordenAPDF.paciente =
					resultPaciente.apellido + ", " + resultPaciente.nombre;

				this.$refs.html2Pdf.generatePdf();
			},

			limpiar_filtro_fecha() {
				this.filter_fecha.desde = null;
				this.filter_fecha.hasta = null;
			},
		},
		beforeMount() {
			this.testFetch();
			this.getSocio();
			this.getProfesional();
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
	.container {
		float: left;
		width: 80%;
	}
	aside {
		float: right;
		width: 20%;
	}
</style>
