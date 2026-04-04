from app.workers.celery_app import celery_app

@celery_app.task(name="app.workers.tasks.sync_all_integrations")
def sync_all_integrations():
    # TODO: iterar sobre todas as integrações ativas e sincronizar
    print("Sincronizando integrações...")

@celery_app.task(name="app.workers.tasks.calculate_metrics")
def calculate_metrics():
    print("Calculando métricas...")
