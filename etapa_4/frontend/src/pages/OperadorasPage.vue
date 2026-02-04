<script setup>
import { ref, watch, onMounted } from 'vue'
import { useOperadoras } from '../composables/useOperadoras'
import DespesasChart from '../components/DespesasChart.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const pagina = ref(1)
const busca = ref('')

const {
  operadoras,
  loading,
  erro,
  totalPaginas,
  carregarOperadoras
} = useOperadoras()

onMounted(() => {
  carregarOperadoras()
})

watch([pagina, busca], () => {
  carregarOperadoras(pagina.value, busca.value)
})

function abrirDetalhe(cnpj) {
  router.push(`/operadora/${cnpj}`)
}
</script>

<template>
  <div class="page">

    <h2>Operadoras de Saúde</h2>

    <input
      v-model="busca"
      placeholder="Buscar por Razão Social ou CNPJ..."
      class="search"
    />

    <p v-if="loading">Carregando dados...</p>

    <p v-if="erro" class="erro">
      {{ erro }}
    </p>

    <table
      v-if="operadoras?.length && !loading"
      class="table"
    >
      <thead>
        <tr>
          <th>CNPJ</th>
          <th>Razão Social</th>
          <th>UF</th>
          <th>Modalidade</th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="op in operadoras"
          :key="op.cnpj"
          @click="abrirDetalhe(op.cnpj)"
          class="table-row-hover"
        >
          <td>{{ op.cnpj }}</td>
          <td>{{ op.razao_social }}</td>
          <td>{{ op.uf }}</td>
          <td>{{ op.modalidade }}</td>
        </tr>
      </tbody>
    </table>

    <p v-if="!operadoras?.length && !loading">
      Nenhuma operadora encontrada.
    </p>

    <div class="paginacao">
      <button :disabled="pagina === 1" @click="pagina--">
        Voltar
      </button>

      <span>Página {{ pagina }} de {{ totalPaginas }}</span>

      <button :disabled="pagina === totalPaginas" @click="pagina++">
        Próxima
      </button>
    </div>

    <section class="grafico">

      <h3>Distribuição de despesas por UF</h3>

      <p class="descricao">
        Este gráfico apresenta a distribuição de despesas por UF.
      </p>

      <DespesasChart />

    </section>

  </div>
</template>
