# Ohms lag
Nu har vi lärt oss om spänning, ström och resistans. Sista biten i pusslet är <u>ohms lag</u>. Den berättar för oss hur de olika elektriska storheterna beror på varandra.

![ohms_lag_cartoon](cartoon.png)

Som figuren visar är det **spänning** som driver **strömmen** framåt, men **resistansen** som begränsar strömmen.

Denna balans beskrivs också av matematik:

$$I=\frac{U}{R}$$
$$U=RI$$
$$R=\frac{U}{I}$$

Alla tre formler är sanna, samtidigt! För att komma ihåg formlerna kan man använda *Ohms triangel*:

![ohms_triangel](triangel.svg)

För att lösa ut en viss storhet täcker man över den med handen och läser vad det står. När man täcker över $U$ med handen, är det enda man kan se $RI$. Det betyder att $U=RI$.

```admonish example title="Exempel: beräkna ström"

Beräkna strömmen $I$ i kretsen.

<img src="ks.svg" style="width: 100%;"></img>

**Lösning:**
$I = U/R$, där $U=5 \volt$ och $R=1000 \ohm$.

Alltså blir svaret

$$I = \frac{5}{1000} = 0.005 \ampere = 5 \milli\ampere$$

```