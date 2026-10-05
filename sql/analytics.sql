SELECT
    ROUND(
        SUM(
            CASE
                WHEN o.transaction_type = 'SALE'
                THEN oi.quantity * oi.unit_price
                ELSE 0
            END
        ),
        2
    ) AS gross_sales,

    ROUND(
        SUM(
            CASE
                WHEN o.transaction_type = 'CANCELLATION'
                THEN oi.quantity * oi.unit_price
                ELSE 0
            END
        ),
        2
    ) AS cancellation_value,

    ROUND(
        SUM(
            CASE
                WHEN o.transaction_type IN ('SALE', 'CANCELLATION')
                THEN oi.quantity * oi.unit_price
                ELSE 0
            END
        ),
        2
    ) AS net_sales

FROM order_items oi

JOIN orders o
    ON oi.invoice_no = o.invoice_no;