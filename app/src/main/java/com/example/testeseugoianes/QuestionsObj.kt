package com.example.testeseugoianes

object QuestionsObj {
    var acertos: Int = 0

    var atual: Int = 0

    val question1: Question = Question("Questão 1", "O que significa \"dar trela\"?", "Ataque de risos", "Ajudar",
                            "Dar Continuidade", "Xavecar", "aut1")

    val question2: Question = Question("Questão 2", "O que significa \"Queijinho\"?", "Queijo Pequeno", "Pessoa que come muito queijo",
        "Rotatória de trânsito", "Rua estreita", "aut3")

    val question3: Question = Question("Questão 3", "O que significa \"Catilanga\"?", "Fedor", "Mulher feia",
        "Mulher alta", "Kombi", "aut2")

    val question4: Question = Question("Questão 4", "O que significa \"Maria Izabel\"?", "Mulher velha", "Mulher alta",
        "Arroz com carne do sol", "Mulher Interesseira", "aut3")

    val question5: Question = Question("Questão 5", "O que significa \"Pulá o Corguim\"?", "Passar dos limites", "Pular o Córrego",
        "Experimentar Algo Novo", "Estar Muito Feliz", "aut1")

    val question6: Question = Question("Questão 6", "O que significa \"Esturdia\"?", "Burrice", "Dia Tranquilo",
        "Hoje de Tarde", "Esses Dias", "aut4")

    val question7: Question = Question("Questão 7", "O que significa \"Fera\"?", "Animal Selvagem", "Pessoa Brava",
        "Bom", "Pessoa Veloz", "aut3")

    val question8: Question = Question("Questão 8", "O que significa \"Rebuçar\"?", "Cobrir", "Ajudar",
        "Assustar", "Supreender", "aut1")

    val question9: Question = Question("Questão 9", "O que significa \"Di Rocha\"?", "Advindo da Rocha", "Confirmar Algo",
        "Negar Algo", "Propor um Assunto", "aut2")

    val question10: Question = Question("Questão 10", "O que significa \"Esbaforido(a)\"?", "Transtornado", "Cançado",
        "Estressado", "Entediado", "aut2")

    val question11: Question = Question("Questão 11", "O que significa \"Invinha\"?", "Uva Pequena", "Tipo de árvore",
        "Enviado", "Algo vindo", "aut4")

    val question12: Question = Question("Questão 12", "O que significa \"Pizêro\"?", "Um Animal", "Vacilo",
        "Bagunça", "Pier", "aut3")

    val question13: Question = Question("Questão 13", "O que significa \"Tunda\"?", "Tipo de Fruta", "Surra",
        "Mata Selvagem", "Planta do Cerrado", "aut2")

    val fim: Question = Question("Fim")


    fun getQuestion(number: Int): Question = when(number) {
        1 -> question1
        2 -> question2
        3 -> question3
        4 -> question4
        5 -> question5
        6 -> question6
        7 -> question7
        8 -> question8
        9 -> question9
        10 -> question10
        11 -> question11
        12 -> question12
        13 -> question13
        else -> fim
    }

    fun addAcerto() = acertos++

    fun checkAcerto(aut: String): Boolean {
        return getQuestion(atual).correct == aut

    }

    fun reset() {
        acertos = 0
        atual = 0
    }

}