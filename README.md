# AI CRACKER

금융사기 예방을 위한 AI Intervention Layer MVP

## Overview

AI CRACKER는 금융거래에서 위험이 탐지된 이후,
사용자가 해당 거래를 왜 안전하다고 믿고 있는지 분석하고
대화와 검증 행동을 통해 사용자의 판단을 재검토하도록 돕는
금융사기 예방 AI 서비스입니다.

본 프로젝트는 실제 금융 고객 데이터 및 개인정보를 사용하지 않습니다.

모든 거래 정보는 MVP를 위한 가상 데이터입니다.

## Core Flow

사용자 송금 시도

↓

Transaction Risk Analysis

↓

High Risk Transaction

↓

AI CRACKER Intervention

↓

Context Decision Tree

↓

Situation & Belief Analysis

↓

JAM Analysis

↓

Verification Action

↓

Final Decision

## Technology

- Python
- Streamlit
- pandas
- Generative AI API
- JSON
- SQLite (optional)

## Run

### 1. Conda 환경 활성화

```bash
conda activate ai-cracker