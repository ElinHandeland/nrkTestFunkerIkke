### NRKCase
<p> Case for NRK. Hente ut data fra Github APIet </p>

#### Kort oppsummering
<p> I denne casen utgitt av NRK har jeg jobbet mot Github APIet for å hente ut data fra ulike personer og organisasjoner sine repository </p>

#### For å bygge prosjektet i Docker
```bash
docker build -t "nrkcase" .
```
#### For å kjøre prosjektet i Docker
```bash
docker run nrkcase --repo="NRK"
```
