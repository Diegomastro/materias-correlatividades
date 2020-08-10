from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from uis import ui_main_window
from etc import *


class VentanaMain:
    def __init__(self):
        # Setup window
        self.this_window = QMainWindow()
        self.ui = ui_main_window.Ui_MainWindow()
        self.ui.setupUi(self.this_window)

        # center
        frame_geometry = self.this_window.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.this_window.move(frame_geometry.topLeft())

        # Show or exec
        self.this_window.show()

        # Conectar materias a sus bottones
        anm1.boton = self.ui.btn_anm1
        alg1.boton = self.ui.btn_alg1
        disc.boton = self.ui.btn_disc
        quim.boton = self.ui.btn_quim
        dibu.boton = self.ui.btn_dibu
        tics.boton = self.ui.btn_tics
        elem.boton = self.ui.btn_elem
        tis.boton = self.ui.btn_tis
        anm2.boton = self.ui.btn_anm2
        alg2.boton = self.ui.btn_alg2
        req.boton = self.ui.btn_req
        arq.boton = self.ui.btn_arq
        prog.boton = self.ui.btn_prog
        fis1.boton = self.ui.btn_fis1
        fis2.boton = self.ui.btn_fis2
        prob.boton = self.ui.btn_prob
        calc.boton = self.ui.btn_calc
        base.boton = self.ui.btn_base
        proga.boton = self.ui.btn_proga
        segu.boton = self.ui.btn_segu
        so.boton = self.ui.btn_so
        ansis.boton = self.ui.btn_ansis
        comu.boton = self.ui.btn_comu
        ingreq.boton = self.ui.btn_ingreq
        dise.boton = self.ui.btn_dise
        answ.boton = self.ui.btn_answ
        soa.boton = self.ui.btn_soa
        redes.boton = self.ui.btn_redes
        leng.boton = self.ui.btn_leng
        gest.boton = self.ui.btn_gest
        ing1.boton = self.ui.btn_ing1
        ing2.boton = self.ui.btn_ing2
        ing3.boton = self.ui.btn_ing3
        ing4.boton = self.ui.btn_ing4
        comp1.boton = self.ui.btn_comp1
        comp2.boton = self.ui.btn_comp2

        # Conectar signals a slots
        self.ui.btn_anm1.clicked.connect(self.on_btn_anm1_clicked)
        self.ui.btn_alg1.clicked.connect(self.on_btn_alg1_clicked)
        self.ui.btn_disc.clicked.connect(self.on_btn_disc_clicked)
        self.ui.btn_quim.clicked.connect(self.on_btn_quim_clicked)
        self.ui.btn_dibu.clicked.connect(self.on_btn_dibu_clicked)
        self.ui.btn_tics.clicked.connect(self.on_btn_tics_clicked)
        self.ui.btn_elem.clicked.connect(self.on_btn_elem_clicked)
        self.ui.btn_tis.clicked.connect(self.on_btn_tis_clicked)
        self.ui.btn_anm2.clicked.connect(self.on_btn_anm2_clicked)
        self.ui.btn_alg2.clicked.connect(self.on_btn_alg2_clicked)
        self.ui.btn_req.clicked.connect(self.on_btn_req_clicked)
        self.ui.btn_arq.clicked.connect(self.on_btn_arq_clicked)
        self.ui.btn_prog.clicked.connect(self.on_btn_prog_clicked)
        self.ui.btn_fis1.clicked.connect(self.on_btn_fis1_clicked)
        self.ui.btn_fis2.clicked.connect(self.on_btn_fis2_clicked)
        self.ui.btn_prob.clicked.connect(self.on_btn_prob_clicked)
        self.ui.btn_calc.clicked.connect(self.on_btn_calc_clicked)
        self.ui.btn_base.clicked.connect(self.on_btn_base_clicked)
        self.ui.btn_proga.clicked.connect(self.on_btn_proga_clicked)
        self.ui.btn_segu.clicked.connect(self.on_btn_segu_clicked)
        self.ui.btn_so.clicked.connect(self.on_btn_so_clicked)
        self.ui.btn_ansis.clicked.connect(self.on_btn_ansis_clicked)
        self.ui.btn_comu.clicked.connect(self.on_btn_comu_clicked)
        self.ui.btn_ingreq.clicked.connect(self.on_btn_ingreq_clicked)
        self.ui.btn_dise.clicked.connect(self.on_btn_dise_clicked)
        self.ui.btn_answ.clicked.connect(self.on_btn_answ_clicked)
        self.ui.btn_soa.clicked.connect(self.on_btn_soa_clicked)
        self.ui.btn_redes.clicked.connect(self.on_btn_redes_clicked)
        self.ui.btn_leng.clicked.connect(self.on_btn_leng_clicked)
        self.ui.btn_gest.clicked.connect(self.on_btn_gest_clicked)
        self.ui.btn_ing1.clicked.connect(self.on_btn_ing1_clicked)
        self.ui.btn_ing2.clicked.connect(self.on_btn_ing2_clicked)
        self.ui.btn_ing3.clicked.connect(self.on_btn_ing3_clicked)
        self.ui.btn_ing4.clicked.connect(self.on_btn_ing4_clicked)
        self.ui.btn_comp1.clicked.connect(self.on_btn_comp1_clicked)
        self.ui.btn_comp2.clicked.connect(self.on_btn_comp2_clicked)

    # todas las funciones de los slots
    def on_btn_anm1_clicked(self):
        print("ANM")
        anm1.aprobada = not anm1.aprobada
        check_correlatividades()

    def on_btn_alg1_clicked(self):
        alg1.aprobada = not alg1.aprobada
        check_correlatividades()

    def on_btn_disc_clicked(self):
        disc.aprobada = not disc.aprobada
        check_correlatividades()

    def on_btn_quim_clicked(self):
        quim.aprobada = not quim.aprobada
        check_correlatividades()

    def on_btn_dibu_clicked(self):
        dibu.aprobada = not dibu.aprobada
        check_correlatividades()

    def on_btn_tics_clicked(self):
        tics.aprobada = not tics.aprobada
        check_correlatividades()

    def on_btn_elem_clicked(self):
        elem.aprobada = not elem.aprobada
        check_correlatividades()

    def on_btn_tis_clicked(self):
        tis.aprobada = not tis.aprobada
        check_correlatividades()

    def on_btn_anm2_clicked(self):
        anm2.aprobada = not anm2.aprobada
        check_correlatividades()

    def on_btn_alg2_clicked(self):
        alg2.aprobada = not alg2.aprobada
        check_correlatividades()

    def on_btn_req_clicked(self):
        req.aprobada = not req.aprobada
        check_correlatividades()

    def on_btn_arq_clicked(self):
        arq.aprobada = not arq.aprobada
        check_correlatividades()

    def on_btn_prog_clicked(self):
        prog.aprobada = not prog.aprobada
        check_correlatividades()

    def on_btn_fis1_clicked(self):
        fis1.aprobada = not fis1.aprobada
        check_correlatividades()

    def on_btn_fis2_clicked(self):
        fis2.aprobada = not fis2.aprobada
        check_correlatividades()

    def on_btn_prob_clicked(self):
        prob.aprobada = not prob.aprobada
        check_correlatividades()

    def on_btn_calc_clicked(self):
        calc.aprobada = not calc.aprobada
        check_correlatividades()

    def on_btn_base_clicked(self):
        base.aprobada = not base.aprobada
        check_correlatividades()

    def on_btn_proga_clicked(self):
        proga.aprobada = not proga.aprobada
        check_correlatividades()

    def on_btn_segu_clicked(self):
        segu.aprobada = not segu.aprobada
        check_correlatividades()

    def on_btn_so_clicked(self):
        so.aprobada = not so.aprobada
        check_correlatividades()

    def on_btn_ansis_clicked(self):
        ansis.aprobada = not ansis.aprobada
        check_correlatividades()

    def on_btn_comu_clicked(self):
        comu.aprobada = not comu.aprobada
        check_correlatividades()

    def on_btn_ingreq_clicked(self):
        ingreq.aprobada = not ingreq.aprobada
        check_correlatividades()

    def on_btn_dise_clicked(self):
        dise.aprobada = not dise.aprobada
        check_correlatividades()

    def on_btn_answ_clicked(self):
        answ.aprobada = not answ.aprobada
        check_correlatividades()

    def on_btn_soa_clicked(self):
        soa.aprobada = not soa.aprobada
        check_correlatividades()

    def on_btn_redes_clicked(self):
        redes.aprobada = not redes.aprobada
        check_correlatividades()

    def on_btn_leng_clicked(self):
        leng.aprobada = not leng.aprobada
        check_correlatividades()

    def on_btn_gest_clicked(self):
        gest.aprobada = not gest.aprobada
        check_correlatividades()

    def on_btn_ing1_clicked(self):
        ing1.aprobada = not ing1.aprobada
        check_correlatividades()

    def on_btn_ing2_clicked(self):
        ing2.aprobada = not ing2.aprobada
        check_correlatividades()

    def on_btn_ing3_clicked(self):
        ing3.aprobada = not ing3.aprobada
        check_correlatividades()

    def on_btn_ing4_clicked(self):
        ing4.aprobada = not ing4.aprobada
        check_correlatividades()

    def on_btn_comp1_clicked(self):
        comp1.aprobada = not comp1.aprobada
        check_correlatividades()

    def on_btn_comp2_clicked(self):
        comp2.aprobada = not comp2.aprobada
        check_correlatividades()
