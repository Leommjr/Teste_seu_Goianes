package com.example.testeseugoianes

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView

class FimActivity : AppCompatActivity() {
    private lateinit var acerts: TextView
    private lateinit var reiniciar: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fim)

        acerts = findViewById(R.id.textAcertos)
        reiniciar = findViewById(R.id.buttonReiniciar)

        val acertos: Int = intent.getIntExtra("ACERTOS", 0)
        acerts.text = acertos.toString()

        reiniciar.setOnClickListener(object : View.OnClickListener {
            override fun onClick(v: View?) {
                QuestionsObj.reset()
                val intent = Intent(this@FimActivity, MainActivity::class.java)
                startActivity(intent)

            }
        })
    }

    override fun onBackPressed() {
        QuestionsObj.reset()
        val intent = Intent(this@FimActivity, MainActivity::class.java)
        startActivity(intent)
    }
}