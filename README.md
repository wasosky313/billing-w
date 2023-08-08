# billing-w
Repository of billing SQLs and annotations

## Separar depois em arquivos SQL

SQLs

----------------------------------------------------------------------
query to take installments from the cpf_cnpj customer

select f.id as financiamento_id, f.identifier as CCB, c.cpf_cnpj as customer_cpf_cnpj, fi.number as parcela_number from financings f, financial_installments fi, customers c 
    where f.customer_id = c.id and c.cpf_cnpj = '018.282.051-33' and f.id = fi.financing_id order by fi.number
    
out -> financiamento_id | CCB | customer_cpf_cnpj | parcela_number

--------------------------------------------------------------------------------


query com data year ( bom para quando o ano é salvado errado tipo '0023')
SELECT count(*)
FROM financial_installments fi, financings f
WHERE fi.financing_id = f.id and f.identifier = 'RA0726956000'
and EXTRACT(YEAR FROM CAST(fi.expire_on AS DATE)) = 0023;

------------------------------------------------------------------------------------------------------------------------
query to select installments withuot billets

  select distinct fi.*, items.status from financial_installments fi
    inner join financings f on f.id  = fi.financing_id 
    left  join bank_billet_creation_batches_items items on items.financial_installment_id = fi.id
    where f.cet = 'PRE_FIXADO'
    and f.status in ('active', 'fraud_cob', 'non_defaulting', 'advanced_billing', 'grace_period', 'fraud_int')
    and fi.status in ('opened', 'expired')
    and fi.securitization in ('fidc1','fidc2','fidc4','fidc5','sec1','amazonia_solar','rural','solfacil','caixa_solfacil')
    and fi.expire_on <= '2023-07-20'
    and (case
        when (select count(*) from bank_billet_creation_batches_items items2



otra para installments
select distinct fi.*, items.status from financial_installments fi
    inner join financings f on f.id  = fi.financing_id
    left  join bank_billet_creation_batches_items items on items.financial_installment_id = fi.id
    where f.cet = 'POS_FIXADO'
    and f.status in ('active', 'fraud_cob', 'non_defaulting', 'advanced_billing', 'grace_period', 'fraud_int')
    and fi.status in ('opened', 'expired')
    and fi.securitization in ('fidc1','fidc2','fidc3','fidc4','fidc5','sec1','amazonia_solar','rural','solfacil','caixa_solfacil')
    and fi.expire_on between '2023-08-08' and '2023-08-23'
    and (case
        when (select count(*) from bank_billet_creation_batches_items items2
        where  items2.financial_installment_id = fi.id and items2.status = 'done') > 0 then false
        when (select count(*) from payments p2
        where  p2.financial_installment_id = fi.id and p2.status <> 'canceled') > 0 then false
        else true
        end);
        where  items2.financial_installment_id = fi.id and items2.status = 'done') > 0 then false
        else true
        end)
-----------------------------------------------------------------------------------------------------------------------------------
