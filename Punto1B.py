def main():
    from matplotlib import pyplot as plt
    from matplotlib_venn import venn3

    A = {30, 50, 0}
    G = {30, 15, 10, 45}
    E = {0, 40, 70, 60}
    print(f"calcule el resultado de (A∪E ꚛ(GUE))")
    #A&C: INTERSECCION
    #A|C: UNION
    #A-C: DIFERENCIA
    #A^C: DIFERENCIA SIMETRICA
    resultado1=(A|E ^(G|E))
    print(f"(A∪E ꚛ(GUE)))= {resultado1}")

    v= venn3((1, 1, 1, 1, 1, 1, 1), set_labels=("A","E","G"))
    v.get_label_by_id("111").set_text(0)
    v.get_label_by_id("100").set_text(A-G-E)
    v.get_label_by_id("010").set_text(E-A-G)
    v.get_label_by_id("001").set_text(G-A-E)
    v.get_label_by_id("110").set_text(A&E)
    v.get_label_by_id("101").set_text(A&G)
    v.get_label_by_id("011").set_text(0)
    plt.show()
main()