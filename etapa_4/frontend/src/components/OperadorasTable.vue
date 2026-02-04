<script setup>
import { ref, watch, onMounted } from 'vue'
import { buscarOperadoras } from '../api/operadoras'

const operadoras = ref([])
const page = ref(1)
const search = ref('')
const loading = ref(false)
const error = ref(null)

async function carregar() {
  loading.value = true
  error.value = null

  try {

    const res = await buscarOperadoras(page.value, search.value)
    operadoras.value = res.data

  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

watch(search, () => {
  page.value = 1
  carregar()
})

onMounted(carregar)
</script>

<template>
  <div class="card">

    <h2>Operadoras</h2>

    <input
      v-model="search"
      placeholder="Buscar por CNPJ ou Razão Social"
      class="search"
    />

    <p v-if="loading">Carregando...</p>
    <p v-if="error">{{ error }}</p>

    <table v-if="operadoras.length">
      <thead>
        <tr>
          <th>CNPJ</th>
          <th>Razão Social</th>
          <th>UF</th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="op in operadoras"
          :key="op.cnpj"
          class="clickable"
        >
          <td>
            <router-link :to="`/operadora/${op.cnpj}`">
              {{ op.cnpj }}
            </router-link>
          </td>

          <td>{{ op.razao_social }}</td>
          <td>{{ op.uf }}</td>
        </tr>
      </tbody>
    </table>

    <p v-if="!loading && !operadoras.length">
      Nenhuma operadora encontrada
    </p>

  </div>
</template>