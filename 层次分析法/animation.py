from manim import *

class EigenvalueStretch(Scene):
    def construct(self):
        # 创建坐标系
        axes = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        self.add(axes)

        # 绘制原始向量
        vector = Vector([2, 1], color=YELLOW)
        vector_label = MathTex(r"\vec{v}", color=YELLOW).next_to(vector.get_end(), RIGHT)
        self.add(vector, vector_label)

        # 定义特征值列表
        eigenvalues = [0.5, 1, 2]

        for eigenvalue in eigenvalues:
            # 定义线性变换矩阵（对角矩阵）
            transformation_matrix = [[eigenvalue, 0],
                                     [0, eigenvalue]]

            # 显示当前特征值
            eigenvalue_text = MathTex(f"\lambda = {eigenvalue}").to_edge(UP)
            self.play(Write(eigenvalue_text))
            self.wait(1)

            # 应用变换前保存原始对象的副本
            axes_copy = axes.copy()
            vector_copy = vector.copy()

            # 应用线性变换
            self.play(
                ApplyMatrix(transformation_matrix, axes_copy),
                ApplyMatrix(transformation_matrix, vector_copy),
                run_time=2
            )
            self.wait(1)

            # 更新向量标签位置
            vector_copy_label = MathTex(r"\lambda \vec{v}", color=YELLOW).next_to(vector_copy.get_end(), RIGHT)
            self.add(vector_copy_label)

            # 显示变换前后的向量坐标
            original_coords = vector.get_end()
            transformed_coords = vector_copy.get_end()
            coords_text = MathTex(
                f"\\vec{{v}} = \\begin{{bmatrix}} {original_coords[0]:.1f} \\\\ {original_coords[1]:.1f} \\end{{bmatrix}}"
                f"\\rightarrow \\lambda \\vec{{v}} = \\begin{{bmatrix}} {transformed_coords[0]:.1f} \\\\ {transformed_coords[1]:.1f} \\end{{bmatrix}}"
            ).next_to(eigenvalue_text, DOWN)
            self.play(Write(coords_text))
            self.wait(2)

            # 移除当前特征值的对象
            self.play(
                FadeOut(axes_copy),
                FadeOut(vector_copy),
                FadeOut(vector_copy_label),
                FadeOut(eigenvalue_text),
                FadeOut(coords_text),
                run_time=1
            )

        self.wait(1)