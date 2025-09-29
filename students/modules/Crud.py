materias_disponibles = set()
estudiantes = {} 


def registrar_estudiante():
    
    id_est = input("ID único del estudiante: ").strip()
    if id_est in estudiantes:
        print("⚠️ Ese ID ya está registrado.")
        return
    nombre = input("Nombre del estudiante: ").strip()
    estudiantes[id_est] = {'nombre': nombre, 'materias': set(), 'calificaciones': {}}
    print(f"✅ Estudiante '{nombre}' ({id_est}) registrado.")


def agregar_materias():
    print("Ingrese materias: ")
    while True:
        m = input("Materia: ").strip()
        if not m:
            break
        materias_disponibles.add(m)
        print(f"  • '{m}' agregada.")
    print("Materias actuales:", ", ".join(sorted(materias_disponibles)) if materias_disponibles else "Ninguna")


def inscribir_estudiante():
    id_est = input("ID del estudiante a inscribir: ").strip()
    est = estudiantes.get(id_est)
    if not est:
        print("⚠️ Estudiante no encontrado.")
        return
    materia = input("Materia a inscribir: ").strip()
    if materia not in materias_disponibles:
        print("⚠️ Esa materia no existe en materias disponibles.")
        return
    est['materias'].add(materia)
    #
    est['calificaciones'].setdefault(materia, [])
    print(f"✅ {est['nombre']} inscrito en '{materia}'.")


def registrar_calificacion():
    id_est = input("ID del estudiante: ").strip()
    est = estudiantes.get(id_est)
    if not est:
        print("⚠️ Estudiante no encontrado.")
        return
    materia = input("Materia: ").strip()
    if materia not in est['materias']:
        print("⚠️ El estudiante no está inscrito en esa materia.")
        return
    try:
        nota = float(input("Nota : ").strip())
    except ValueError:
        print("⚠️ Nota inválida.")
        return
    
    est['calificaciones'].setdefault(materia, []).append(nota)
    print(f"✅ Nota {nota} registrada para {est['nombre']} en '{materia}'.")


def ver_materias_comunes():
    id1 = input("ID primer estudiante: ").strip()
    id2 = input("ID segundo estudiante: ").strip()
    e1 = estudiantes.get(id1)
    e2 = estudiantes.get(id2)
    if not e1 or not e2:
        print("⚠️ Alguno de los estudiantes no existe.")
        return
    comunes = e1['materias'].intersection(e2['materias'])
    if comunes:
        print("Materias comunes:", ", ".join(sorted(comunes)))
    else:
        print("No tienen materias en común.")


def operaciones_conjuntos():
    
    id1 = input("ID primer estudiante: ").strip()
    id2 = input("ID segundo estudiante: ").strip()
    e1 = estudiantes.get(id1)
    e2 = estudiantes.get(id2)
    if not e1 or not e2:
        print("⚠️ Alguno de los estudiantes no existe.")
        return
    s1 = e1['materias']
    s2 = e2['materias']
    print(f"{e1['nombre']} materias: {', '.join(sorted(s1)) if s1 else 'Ninguna'}")
    print(f"{e2['nombre']} materias: {', '.join(sorted(s2)) if s2 else 'Ninguna'}")
    print("Intersección (& / .intersection()):", ", ".join(sorted(s1 & s2)) or "Ninguna")
    print("Unión (| / .union()):", ", ".join(sorted(s1 | s2)) or "Ninguna")
    print(f"Diferencia {e1['nombre']} - {e2['nombre']}:", ", ".join(sorted(s1 - s2)) or "Ninguna")
    print(f"Diferencia {e2['nombre']} - {e1['nombre']}:", ", ".join(sorted(s2 - s1)) or "Ninguna")


def generar_reporte():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\n--- Promedios por estudiante y materia ---")
    for id_est, datos in estudiantes.items():
        nombre = datos['nombre']
        cal_dict = datos['calificaciones'] 
        print(f"\nEstudiante: {nombre} (ID: {id_est})")
        tot_all = 0.0
        count_all = 0
        if not cal_dict:
            print("  Sin calificaciones.")
            continue
        for materia, notas in cal_dict.items():
            if notas:
                promedio = sum(notas) / len(notas)
                print(f"  {materia}: {promedio:.2f}  (notas: {notas})")
                tot_all += sum(notas)
                count_all += len(notas)
            else:
                print(f"  {materia}: Sin notas.")
        if count_all:
            print(f"  Promedio general del estudiante: {tot_all / count_all:.2f}")
        else:
            print("  No hay notas para calcular promedio general.")
    
    print("\n--- Promedio por materia (entre todos los estudiantes) ---")
    if not materias_disponibles:
        print("No hay materias registradas.")
        return
    for materia in sorted(materias_disponibles):
        notas_mat = []
        for datos in estudiantes.values():
            notas = datos['calificaciones'].get(materia, [])
            notas_mat.extend(notas)
        if notas_mat:
            print(f"  {materia}: {sum(notas_mat)/len(notas_mat):.2f} (basado en {len(notas_mat)} nota(s))")
        else:
            print(f"  {materia}: Sin notas registradas.")


def listar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes.")
        return
    
    print("Estudiantes registrados:")
    for id_est, datos in estudiantes.items():
        print(f" - {id_est}: {datos['nombre']} (Materias: {', '.join(sorted(datos['materias'])) or 'Ninguna'})")


def listar_materias():
    if not materias_disponibles:
        print("No hay materias disponibles.")
    else:
        print("Materias disponibles:", ", ".join(sorted(materias_disponibles)))