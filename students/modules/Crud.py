

estudiantes = {}
materias_disponibles = set()



def registrar_estudiante(estudiantes, id_estudiante, nombre):
    estudiantes.setdefault(id_estudiante, {"nombre": nombre, "materias": {}})
    print(f"✅ Estudiante {nombre} (ID: {id_estudiante}) registrado.")

def agregar_materia(materias_disponibles, materia):
    materias_disponibles.add(materia)
    print(f"✅ Materia '{materia}' agregada al sistema.")

def inscribir_estudiante(estudiantes, id_estudiante, materia, materias_disponibles):
    if id_estudiante not in estudiantes:
        print("❌ El estudiante no existe.")
        return
    if materia in materias_disponibles:
        estudiantes[id_estudiante]["materias"].setdefault(materia, [])
        print(f"✅ Estudiante inscrito en {materia}.")
    else:
        print(f"❌ La materia {materia} no está disponible.")

def registrar_calificacion(estudiantes, id_estudiante, materia, nota):
    if id_estudiante not in estudiantes:
        print("❌ El estudiante no existe.")
        return
    if materia in estudiantes[id_estudiante]["materias"]:
        estudiantes[id_estudiante]["materias"][materia].append(nota)
        print(f"✅ Nota {nota} registrada en {materia} para {estudiantes[id_estudiante]['nombre']}.")
    else:
        print(f"❌ El estudiante no está inscrito en {materia}.")

def materias_comunes(estudiantes, id1, id2):
    if id1 not in estudiantes or id2 not in estudiantes:
        print("❌ Uno de los estudiantes no existe.")
        return set()
    m1 = set(estudiantes[id1]["materias"].keys())
    m2 = set(estudiantes[id2]["materias"].keys())
    comunes = m1 & m2
    return comunes

def generar_reporte(estudiantes):
    if not estudiantes:
        print("⚠️ No hay estudiantes registrados.")
        return
    for id_est, datos in estudiantes.items():
        print(f"\n📘 Reporte de {datos['nombre']} (ID: {id_est})")
        if not datos["materias"]:
            print(" - No tiene materias inscritas.")
            continue
        for materia, notas in datos["materias"].items():
            if notas:
                promedio = sum(notas) / len(notas)
                print(f" - {materia}: {notas} → Promedio: {promedio:.2f}")
            else:
                print(f" - {materia}: Sin notas registradas")


   
