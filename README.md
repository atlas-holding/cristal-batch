# ${{ values.name }}

${{ values.description }}

Déployé sur DxP -- golden path `devops/cron` (pattern `scheduled`).

## Planning

Par défaut, ce job s'exécute toutes les 5 minutes (`*/5 * * * *`). Pour
changer la fréquence, modifiez `spec.schedule` dans `k8s/cronjob.yaml` et
poussez le changement -- ArgoCD synchronisera automatiquement.

## Backend référencé

Si un service backend a été référencé à la création (`service-ref`,
nature `pod`), son URL interne est disponible dans la variable d'env
`BACKEND_URL` au sein du conteneur.
