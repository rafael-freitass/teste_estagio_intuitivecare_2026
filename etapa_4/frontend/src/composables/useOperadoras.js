import { ref } from 'vue'
import { buscarOperadoras } from '../api/operadoras'

export function useOperadoras() {

  const operadoras = ref([])
  const loading = ref(false)
  const erro = ref(null)

  const totalPaginas = ref(1)
  const limit = 10

  async function carregarOperadoras(page = 1, search = '') {

    try {

      loading.value = true
      erro.value = null

      const data = await buscarOperadoras(page, search)

      operadoras.value = data.data

      totalPaginas.value = Math.ceil(data.total / limit)

    } catch (e) {
      erro.value = e.message
    } finally {
      loading.value = false
    }
  }

  return {
    operadoras,
    loading,
    erro,
    totalPaginas,
    carregarOperadoras
  }
}