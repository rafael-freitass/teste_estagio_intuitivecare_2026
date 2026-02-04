<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  buscarOperadora,
  buscarDespesasOperadora
} from '../api/operadoras'

const route = useRoute()
const router = useRouter()

const operadora = ref(null)
const despesas = ref([])

const loading = ref(true)
const error = ref(null)

function formatarMoeda(valor) {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL'
  }).format(valor)
}

onMounted(async () => {
  try {
    const cnpj = route.params.cnpj

    operadora.value = await buscarOperadora(cnpj)
    despesas.value = await buscarDespesasOperadora(cnpj) || []

  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="container">

    <button class="voltar" @click="router.back()">
      ← Voltar
    </button>

    <p v-if="loading">Carregando...</p>
    <p v-if="error" class="erro">{{ error }}</p>

    <div v-if="operadora" class="card">

      <h1>{{ operadora.razao_social }}</h1>

      <p><b>CNPJ:</b> {{ operadora.cnpj }}</p>
      <p><b>Modalidade:</b> {{ operadora.modalidade }}</p>
      <p><b>UF:</b> {{ operadora.uf }}</p>

    </div>

    <div class="card">

      <h2>Histórico de Despesas</h2>

      <table v-if="despesas?.length" class="table">
        <thead>
          <tr>
            <th>Ano</th>
            <th>Total</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="d in despesas" :key="d.id">
            <td>{{ d.ano }}</td>
            <td>{{ formatarMoeda(d.valor_despesas) }}</td>
          </tr>
        </tbody>
      </table>

      <p v-else>
        Nenhuma despesa registrada
      </p>

    </div>

  </div>
</template>