def main():
    from matplotlib import pyplot as plt
    from matplotlib_venn import venn2

    B = {15, 100, 40}
    G = {30, 15, 10, 45}
    print(f"calcule el resultado de (B∪G)")
    #A&C: INTERSECCION
    #A|C: UNION
    #A-C: DIFERENCIA
    #A^C: DIFERENCIA SIMETRICA
    resultado1=(B-G)
    print(f"(B∪G)= {resultado1}")

    v= venn2((1, 1, 1), set_labels=("B","G"))
    v.get_label_by_id("11").set_text(B&G)
    v.get_label_by_id("10").set_text(B-G)
    v.get_label_by_id("01").set_text(G-B)
    v.get_label_by_id("11").set_color("#FF0000")
    plt.show()
main()