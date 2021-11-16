package com.example.testeseugoianes


import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.view.View
import android.widget.CheckBox
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class QuestionsActivity : AppCompatActivity() {
    private lateinit var title: TextView
    private lateinit var desc: TextView
    private lateinit var aut1: CheckBox
    private lateinit var aut2: CheckBox
    private lateinit var aut3: CheckBox
    private lateinit var aut4: CheckBox


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_questions)

        title = findViewById(R.id.textTitle)
        desc = findViewById(R.id.textDesc)
        aut1 = findViewById(R.id.checkBox1)
        aut2 = findViewById(R.id.checkBox2)
        aut3 = findViewById(R.id.checkBox3)
        aut4 = findViewById(R.id.checkBox4)
        val question: Int = intent.getIntExtra("QUESTION", 0)
        setQuestion(question)
        if(QuestionsObj.getQuestion(question).title == "Fim") {
            val intent = Intent(this@QuestionsActivity, FimActivity::class.java).apply {
                putExtra("ACERTOS", (QuestionsObj.acertos))
            }
            startActivity(intent)
        }
        QuestionsObj.atual = question
        }

    fun setQuestion(id: Int) {
        title.text = QuestionsObj.getQuestion(id).title
        desc.text = QuestionsObj.getQuestion(id).desc
        aut1.text = QuestionsObj.getQuestion(id).aut1
        aut2.text = QuestionsObj.getQuestion(id).aut2
        aut3.text = QuestionsObj.getQuestion(id).aut3
        aut4.text = QuestionsObj.getQuestion(id).aut4
    }

    fun onCheckboxClicked(view: View) {
        if (view is CheckBox) {
            val checked: Boolean = view.isChecked

            when (view.id) {
                R.id.checkBox1 -> {
                    if (checked) {
                        if(QuestionsObj.checkAcerto("aut1")) {
                            QuestionsObj.addAcerto()
                            aut1.setTextColor(Color.GREEN)
                        }
                        else {
                            aut1.setTextColor(Color.RED)
                        }
                    }
                }
                R.id.checkBox2 -> {
                    if (checked) {
                        if(QuestionsObj.checkAcerto("aut2")) {
                            QuestionsObj.addAcerto()
                            aut2.setTextColor(Color.GREEN)
                        }
                        else {
                            aut2.setTextColor(Color.RED)
                        }
                    }
                }
                R.id.checkBox3 -> {
                    if (checked) {
                        if(QuestionsObj.checkAcerto("aut3")) {
                            QuestionsObj.addAcerto()
                            aut3.setTextColor(Color.GREEN)
                        }
                        else {
                            aut3.setTextColor(Color.RED)
                        }
                    }
                }
                R.id.checkBox4 -> {
                    if (checked) {
                        if(QuestionsObj.checkAcerto("aut4")) {
                            QuestionsObj.addAcerto()
                            aut4.setTextColor(Color.GREEN)
                        }
                        else {
                            aut4.setTextColor(Color.RED)
                        }
                    }
                }
            }
            val intent = Intent(this@QuestionsActivity, QuestionsActivity::class.java).apply {
                putExtra("QUESTION", (QuestionsObj.atual+1))
            }
            startActivity(intent)
        }
    }

    override fun onBackPressed() {
        Toast.makeText(this@QuestionsActivity, "Não pode voltar!!\n Termina o questionário.", Toast.LENGTH_SHORT).show()

    }
}