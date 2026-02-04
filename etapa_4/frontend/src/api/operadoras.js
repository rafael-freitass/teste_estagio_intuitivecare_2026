const BASE_URL = import.meta.env.VITE_API_URL

export async function buscarOperadoras(page = 1, search = '') {

  const params = new URLSearchParams({
    page,
    limit: 10,
    search
  })

  const res = await fetch(`${BASE_URL}/operadoras?${params}`)

  if (!res.ok) throw new Error('Erro ao buscar operadoras')

  return res.json()
}


export async function buscarOperadora(cnpj) {

  const res = await fetch(`${BASE_URL}/operadoras/${cnpj}`)

  if (!res.ok) throw new Error('Erro ao buscar operadora')

  return res.json()
}


export async function buscarDespesasOperadora(cnpj) {

  const res = await fetch(`${BASE_URL}/operadoras/${cnpj}/despesas`)

  if (!res.ok) throw new Error('Erro ao buscar despesas')

  return res.json()
}


export async function buscarEstatisticas() {

  const res = await fetch(`${BASE_URL}/estatisticas`)

  if (!res.ok) throw new Error('Erro ao buscar estatísticas')

  return res.json()
}

export async function buscarDespesasPorUF() {

  const res = await fetch(`${BASE_URL}/estatisticas/despesas-por-uf`)

  if (!res.ok) throw new Error('Erro ao buscar despesas por UF')

  return res.json()
}