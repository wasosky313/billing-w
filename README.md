# billing-w
Repository of billing SQLs and annotations

SQLs

----------------------------------------------------------------------
query to take installments from the cpf_cnpj customer

select f.id as financiamento_id, f.identifier as CCB, c.cpf_cnpj as customer_cpf_cnpj, fi.number as parcela_number from financings f, financial_installments fi, customers c 
    where f.customer_id = c.id and c.cpf_cnpj = '018.282.051-33' and f.id = fi.financing_id order by fi.number
    
out -> financiamento_id | CCB | customer_cpf_cnpj | parcela_number

--------------------------------------------------------------------------------
