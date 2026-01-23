"""
BACBB 논문 다이어그램 v2 - 프로페셔널 디자인
깔끔하고 모던한 스타일
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon
from matplotlib.patches import ConnectionPatch
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# 폰트 설정
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.unicode_minus'] = False

print("="*70)
print("BACBB 프로페셔널 다이어그램 생성 v2")
print("="*70)

# 색상 팔레트 (모던 & 다크테마 친화적)
COLORS = {
    'bg': '#FFFFFF',
    'primary': '#2563EB',      # Blue
    'secondary': '#7C3AED',    # Purple
    'success': '#059669',      # Green
    'danger': '#DC2626',       # Red
    'warning': '#D97706',      # Orange
    'info': '#0891B2',         # Cyan
    'dark': '#1F2937',
    'gray': '#6B7280',
    'light_gray': '#F3F4F6',
    'box_blue': '#DBEAFE',
    'box_purple': '#EDE9FE',
    'box_green': '#D1FAE5',
    'box_red': '#FEE2E2',
    'box_orange': '#FEF3C7',
    'box_cyan': '#CFFAFE',
}

def draw_rounded_box(ax, x, y, w, h, text, bg_color, border_color, 
                     fontsize=10, text_color='#1F2937', bold=False, 
                     subtitle=None, icon=None):
    """깔끔한 둥근 박스 그리기"""
    box = FancyBboxPatch((x, y), w, h, 
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=bg_color, edgecolor=border_color, 
                         linewidth=2, alpha=0.95)
    ax.add_patch(box)
    
    weight = 'bold' if bold else 'normal'
    if subtitle:
        ax.text(x + w/2, y + h*0.65, text, ha='center', va='center', 
                fontsize=fontsize, fontweight=weight, color=text_color)
        ax.text(x + w/2, y + h*0.35, subtitle, ha='center', va='center', 
                fontsize=fontsize-2, color=COLORS['gray'])
    else:
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
                fontsize=fontsize, fontweight=weight, color=text_color, wrap=True)

def draw_arrow(ax, start, end, color=None, style='->', lw=2, curved=False):
    """화살표 그리기"""
    if color is None:
        color = COLORS['gray']
    
    if curved:
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                   connectionstyle="arc3,rad=0.2"))
    else:
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle=style, color=color, lw=lw))

def draw_label(ax, x, y, text, fontsize=11, color=None, bold=True):
    """라벨 텍스트"""
    if color is None:
        color = COLORS['dark']
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, fontsize=fontsize, fontweight=weight, color=color)


# =============================================================================
# Figure 1: BACBB 전략 로직 구조도 (프로페셔널 버전)
# =============================================================================
print("\n[1] BACBB 전략 로직 구조도 생성 중...")

fig, ax = plt.subplots(figsize=(18, 13), facecolor=COLORS['bg'])
ax.set_xlim(0, 18)
ax.set_ylim(0, 13)
ax.axis('off')
ax.set_facecolor(COLORS['bg'])

# 제목
ax.text(9, 12.5, 'BACBB Strategy Architecture', ha='center', fontsize=20, 
        fontweight='bold', color=COLORS['dark'])
ax.text(9, 12.0, 'Betting Against Cryptocurrency Bad Beta', ha='center', 
        fontsize=12, color=COLORS['gray'])

# ===== STEP 1: Data Input =====
draw_label(ax, 0.5, 10.8, '01  DATA INPUT', color=COLORS['primary'])
ax.plot([0.5, 17.5], [10.6, 10.6], color=COLORS['light_gray'], lw=1)

boxes_step1 = [
    (0.5, 9.3, 3.8, 1.1, 'Crypto Prices', 'Daily OHLCV Data'),
    (4.7, 9.3, 3.8, 1.1, 'Market Cap', 'Volume Weights'),
    (8.9, 9.3, 3.8, 1.1, 'Treasury Rates', '3M / 10Y Yields'),
    (13.1, 9.3, 3.8, 1.1, 'Valuation', '100-week Returns'),
]

for x, y, w, h, title, sub in boxes_step1:
    draw_rounded_box(ax, x, y, w, h, title, COLORS['box_blue'], 
                     COLORS['primary'], fontsize=11, bold=True, subtitle=sub)

# ===== STEP 2: VAR Model =====
draw_label(ax, 0.5, 8.5, '02  VAR(1) MODEL', color=COLORS['secondary'])
ax.plot([0.5, 17.5], [8.3, 8.3], color=COLORS['light_gray'], lw=1)

# VAR 박스
var_box = FancyBboxPatch((0.5, 6.5), 12, 1.5, 
                          boxstyle="round,pad=0.02,rounding_size=0.15",
                          facecolor=COLORS['box_purple'], 
                          edgecolor=COLORS['secondary'], linewidth=2)
ax.add_patch(var_box)

ax.text(6.5, 7.6, 'State Variables', ha='center', fontsize=12, 
        fontweight='bold', color=COLORS['secondary'])

# 상태변수들
vars_info = [
    (2, 'z₁', 'Market Excess Return'),
    (6.5, 'z₂', 'Term Spread'),
    (11, 'z₃', 'Valuation Indicator'),
]
for x, var, desc in vars_info:
    ax.text(x, 7.1, var, ha='center', fontsize=14, fontweight='bold', 
            color=COLORS['dark'])
    ax.text(x, 6.75, desc, ha='center', fontsize=9, color=COLORS['gray'])

# VAR 수식 박스
formula_box = FancyBboxPatch((13, 6.5), 4.5, 1.5, 
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='white', edgecolor=COLORS['gray'], 
                              linewidth=1.5)
ax.add_patch(formula_box)
ax.text(15.25, 7.5, 'VAR Equation', ha='center', fontsize=10, 
        fontweight='bold', color=COLORS['dark'])
ax.text(15.25, 7.0, 'zₜ₊₁ = c + A·zₜ + uₜ₊₁', ha='center', fontsize=11, 
        style='italic', color=COLORS['dark'])

# 화살표: Step1 -> Step2
for i, (x, _, _, _, _, _) in enumerate(boxes_step1):
    draw_arrow(ax, (x + 1.9, 9.3), (2 + i*3.5, 8.0), COLORS['gray'])

# ===== STEP 3: Campbell-Shiller Decomposition =====
draw_label(ax, 0.5, 5.8, '03  CAMPBELL-SHILLER DECOMPOSITION', color=COLORS['success'])
ax.plot([0.5, 17.5], [5.6, 5.6], color=COLORS['light_gray'], lw=1)

# CF News
draw_rounded_box(ax, 0.5, 3.8, 5.5, 1.5, 'Cash-Flow News (NCF)', 
                 COLORS['box_red'], COLORS['danger'], fontsize=12, bold=True,
                 subtitle='Permanent Shock', text_color=COLORS['danger'])

# DR News
draw_rounded_box(ax, 6.5, 3.8, 5.5, 1.5, 'Discount Rate News (NDR)', 
                 COLORS['box_green'], COLORS['success'], fontsize=12, bold=True,
                 subtitle='Transitory Shock', text_color=COLORS['success'])

# 화살표: VAR -> News
draw_arrow(ax, (4, 6.5), (3.25, 5.3), COLORS['danger'])
draw_arrow(ax, (8.5, 6.5), (9.25, 5.3), COLORS['success'])

# ===== STEP 4: Beta Estimation =====
draw_label(ax, 0.5, 3.0, '04  BETA ESTIMATION', color=COLORS['warning'])
ax.plot([0.5, 17.5], [2.8, 2.8], color=COLORS['light_gray'], lw=1)

# CF Beta
draw_rounded_box(ax, 0.5, 1.2, 5.5, 1.4, 'Cash-Flow Beta (βCF)', 
                 COLORS['box_red'], COLORS['danger'], fontsize=11, bold=True,
                 subtitle='Cov(rᵢ, NCF) / Var(NCF)', text_color=COLORS['danger'])
ax.text(3.25, 0.9, '"BAD BETA"', ha='center', fontsize=10, 
        fontweight='bold', color=COLORS['danger'])

# FP Beta
draw_rounded_box(ax, 6.5, 1.2, 5.5, 1.4, 'FP Beta (βFP)', 
                 COLORS['box_green'], COLORS['success'], fontsize=11, bold=True,
                 subtitle='ρ × (σᵢ / σₘ)', text_color=COLORS['success'])
ax.text(9.25, 0.9, '"TOTAL BETA"', ha='center', fontsize=10, 
        fontweight='bold', color=COLORS['success'])

# 화살표: News -> Beta
draw_arrow(ax, (3.25, 3.8), (3.25, 2.6), COLORS['danger'])
draw_arrow(ax, (9.25, 3.8), (9.25, 2.6), COLORS['success'])

# ===== STEP 5: Portfolio Construction =====
draw_label(ax, 13, 5.8, '05  PORTFOLIO', color=COLORS['info'])

# Long 박스
long_box = FancyBboxPatch((13, 4.2), 4.5, 1.2, 
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#DCFCE7', edgecolor='#16A34A', linewidth=2)
ax.add_patch(long_box)
ax.text(15.25, 5.0, 'LONG 70%', ha='center', fontsize=11, 
        fontweight='bold', color='#16A34A')
ax.text(15.25, 4.5, 'Low βCF Assets', ha='center', fontsize=10, color=COLORS['gray'])

# Short 박스
short_box = FancyBboxPatch((13, 2.7), 4.5, 1.2, 
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#FEE2E2', edgecolor='#DC2626', linewidth=2)
ax.add_patch(short_box)
ax.text(15.25, 3.5, 'SHORT 30%', ha='center', fontsize=11, 
        fontweight='bold', color='#DC2626')
ax.text(15.25, 3.0, 'High βCF Assets', ha='center', fontsize=10, color=COLORS['gray'])

# 화살표: Beta -> Portfolio
draw_arrow(ax, (6, 1.9), (13, 4.8), COLORS['gray'], curved=True)
draw_arrow(ax, (6, 1.9), (13, 3.3), COLORS['gray'], curved=True)

# ===== STEP 6: Result =====
result_box = FancyBboxPatch((13, 0.5), 4.5, 1.8, 
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#FEF3C7', edgecolor='#D97706', linewidth=3)
ax.add_patch(result_box)
ax.text(15.25, 1.9, 'BACBB RETURN', ha='center', fontsize=12, 
        fontweight='bold', color='#D97706')
ax.text(15.25, 1.4, 'Sharpe 1.04 | t-stat 2.79***', ha='center', 
        fontsize=10, color=COLORS['dark'])
ax.text(15.25, 0.9, 'MDD -16.15%', ha='center', fontsize=10, color=COLORS['gray'])

# 화살표: Portfolio -> Result
draw_arrow(ax, (15.25, 2.7), (15.25, 2.3), COLORS['warning'])

# 수식 박스 (하단)
formula_main = FancyBboxPatch((0.5, 0.1), 11.5, 0.7, 
                               boxstyle="round,pad=0.02,rounding_size=0.1",
                               facecolor=COLORS['light_gray'], 
                               edgecolor=COLORS['gray'], linewidth=1)
ax.add_patch(formula_main)
ax.text(6.25, 0.45, 'rBACBB = wL·βL⁻¹·(rL - rf - f) - wS·βH⁻¹·(rH - rf - f)', 
        ha='center', fontsize=11, style='italic', color=COLORS['dark'])

plt.tight_layout()
plt.savefig('Figure_BACBB_Logic_Flow.png', dpi=250, bbox_inches='tight', 
            facecolor=COLORS['bg'], pad_inches=0.3)
plt.close()
print("  Figure_BACBB_Logic_Flow.png 저장 완료")



# =============================================================================
# Figure 2: Campbell-Shiller 분해 (프로페셔널 버전)
# =============================================================================
print("\n[2] Campbell-Shiller 분해 다이어그램 생성 중...")

fig, ax = plt.subplots(figsize=(16, 11), facecolor=COLORS['bg'])
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')
ax.set_facecolor(COLORS['bg'])

# 제목
ax.text(8, 10.5, 'Campbell-Shiller Decomposition', ha='center', fontsize=20, 
        fontweight='bold', color=COLORS['dark'])
ax.text(8, 10.0, 'Decomposing Market Returns into News Components', ha='center', 
        fontsize=12, color=COLORS['gray'])

# ===== 상단: Market Return =====
market_box = FancyBboxPatch((5.5, 8.2), 5, 1.3, 
                             boxstyle="round,pad=0.02,rounding_size=0.15",
                             facecolor=COLORS['box_blue'], 
                             edgecolor=COLORS['primary'], linewidth=3)
ax.add_patch(market_box)
ax.text(8, 9.1, 'Market Return', ha='center', fontsize=14, 
        fontweight='bold', color=COLORS['primary'])
ax.text(8, 8.6, 'rₘ,ₜ₊₁ - E[rₘ,ₜ₊₁]', ha='center', fontsize=12, 
        style='italic', color=COLORS['dark'])

# 분해 표시
ax.text(8, 7.6, 'DECOMPOSITION', ha='center', fontsize=11, 
        fontweight='bold', color=COLORS['gray'],
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                  edgecolor=COLORS['gray'], linewidth=1))

# 화살표
draw_arrow(ax, (6.5, 8.2), (4, 6.8), COLORS['danger'], lw=2.5)
draw_arrow(ax, (9.5, 8.2), (12, 6.8), COLORS['success'], lw=2.5)

# ===== Cash-Flow News =====
cf_box = FancyBboxPatch((1, 4.5), 6, 2.3, 
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=COLORS['box_red'], 
                         edgecolor=COLORS['danger'], linewidth=2.5)
ax.add_patch(cf_box)

ax.text(4, 6.4, 'Cash-Flow News', ha='center', fontsize=14, 
        fontweight='bold', color=COLORS['danger'])
ax.text(4, 5.9, 'NCF,t+1', ha='center', fontsize=16, 
        fontweight='bold', color=COLORS['dark'])
ax.text(4, 5.3, 'Permanent Fundamental Shock', ha='center', 
        fontsize=10, color=COLORS['gray'])
ax.text(4, 4.85, '• Irreversible value change', ha='center', 
        fontsize=9, color=COLORS['gray'])

# ===== Discount Rate News =====
dr_box = FancyBboxPatch((9, 4.5), 6, 2.3, 
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=COLORS['box_green'], 
                         edgecolor=COLORS['success'], linewidth=2.5)
ax.add_patch(dr_box)

ax.text(12, 6.4, 'Discount Rate News', ha='center', fontsize=14, 
        fontweight='bold', color=COLORS['success'])
ax.text(12, 5.9, 'NDR,t+1', ha='center', fontsize=16, 
        fontweight='bold', color=COLORS['dark'])
ax.text(12, 5.3, 'Transitory Rate Shock', ha='center', 
        fontsize=10, color=COLORS['gray'])
ax.text(12, 4.85, '• Mean-reverting change', ha='center', 
        fontsize=9, color=COLORS['gray'])

# ===== 핵심 수식 =====
formula_box = FancyBboxPatch((3, 3.0), 10, 1.2, 
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor=COLORS['box_orange'], 
                              edgecolor=COLORS['warning'], linewidth=2)
ax.add_patch(formula_box)
ax.text(8, 3.85, 'Core Identity', ha='center', fontsize=10, 
        fontweight='bold', color=COLORS['warning'])
ax.text(8, 3.35, 'rₜ₊₁ - E[rₜ₊₁] = NCF,t+1 - NDR,t+1', ha='center', 
        fontsize=14, style='italic', color=COLORS['dark'])

# ===== Beta 분해 =====
ax.text(8, 2.4, 'BETA DECOMPOSITION', ha='center', fontsize=11, 
        fontweight='bold', color=COLORS['gray'])
ax.plot([3, 13], [2.2, 2.2], color=COLORS['light_gray'], lw=1)

# CF Beta
cf_beta = FancyBboxPatch((1, 0.5), 6, 1.5, 
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=COLORS['box_red'], 
                          edgecolor=COLORS['danger'], linewidth=2)
ax.add_patch(cf_beta)
ax.text(4, 1.65, 'Cash-Flow Beta (βCF)', ha='center', fontsize=12, 
        fontweight='bold', color=COLORS['danger'])
ax.text(4, 1.15, 'βCF = Cov(rᵢ, NCF) / Var(NCF)', ha='center', 
        fontsize=10, style='italic', color=COLORS['dark'])
ax.text(4, 0.7, '"BAD BETA" - Higher Risk Premium', ha='center', 
        fontsize=9, fontweight='bold', color=COLORS['danger'])

# DR Beta
dr_beta = FancyBboxPatch((9, 0.5), 6, 1.5, 
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=COLORS['box_green'], 
                          edgecolor=COLORS['success'], linewidth=2)
ax.add_patch(dr_beta)
ax.text(12, 1.65, 'Discount Rate Beta (βDR)', ha='center', fontsize=12, 
        fontweight='bold', color=COLORS['success'])
ax.text(12, 1.15, 'βDR = Cov(rᵢ, NDR) / Var(NDR)', ha='center', 
        fontsize=10, style='italic', color=COLORS['dark'])
ax.text(12, 0.7, '"GOOD BETA" - Lower Risk Premium', ha='center', 
        fontsize=9, fontweight='bold', color=COLORS['success'])

# 화살표
draw_arrow(ax, (4, 4.5), (4, 2.0), COLORS['danger'])
draw_arrow(ax, (12, 4.5), (12, 2.0), COLORS['success'])

plt.tight_layout()
plt.savefig('Figure_Campbell_Shiller_Decomposition.png', dpi=250, 
            bbox_inches='tight', facecolor=COLORS['bg'], pad_inches=0.3)
plt.close()
print("  Figure_Campbell_Shiller_Decomposition.png 저장 완료")


# =============================================================================
# Figure 3: 펀딩비 메커니즘 (프로페셔널 버전)
# =============================================================================
print("\n[3] 펀딩비 메커니즘 다이어그램 생성 중...")

fig, ax = plt.subplots(figsize=(16, 11), facecolor=COLORS['bg'])
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')
ax.set_facecolor(COLORS['bg'])

# 제목
ax.text(8, 10.5, 'Perpetual Futures Funding Rate Mechanism', ha='center', 
        fontsize=20, fontweight='bold', color=COLORS['dark'])
ax.text(8, 10.0, 'Price Convergence through Funding Payments', ha='center', 
        fontsize=12, color=COLORS['gray'])

# ===== 가격 비교 섹션 =====
ax.text(8, 9.2, 'PRICE RELATIONSHIP', ha='center', fontsize=11, 
        fontweight='bold', color=COLORS['gray'])

# Spot Price
spot_box = FancyBboxPatch((1, 7.8), 4.5, 1.2, 
                           boxstyle="round,pad=0.02,rounding_size=0.15",
                           facecolor=COLORS['box_blue'], 
                           edgecolor=COLORS['primary'], linewidth=2.5)
ax.add_patch(spot_box)
ax.text(3.25, 8.6, 'Spot Price', ha='center', fontsize=13, 
        fontweight='bold', color=COLORS['primary'])
ax.text(3.25, 8.1, 'Current Market Price', ha='center', fontsize=10, 
        color=COLORS['gray'])

# Perpetual Price
perp_box = FancyBboxPatch((10.5, 7.8), 4.5, 1.2, 
                           boxstyle="round,pad=0.02,rounding_size=0.15",
                           facecolor=COLORS['box_purple'], 
                           edgecolor=COLORS['secondary'], linewidth=2.5)
ax.add_patch(perp_box)
ax.text(12.75, 8.6, 'Perpetual Price', ha='center', fontsize=13, 
        fontweight='bold', color=COLORS['secondary'])
ax.text(12.75, 8.1, 'Futures Contract Price', ha='center', fontsize=10, 
        color=COLORS['gray'])

# 양방향 화살표
ax.annotate('', xy=(10.3, 8.4), xytext=(5.7, 8.4),
            arrowprops=dict(arrowstyle='<->', color=COLORS['dark'], lw=3))
ax.text(8, 8.7, 'Funding Rate', ha='center', fontsize=11, 
        fontweight='bold', color=COLORS['dark'],
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                  edgecolor=COLORS['gray']))

# ===== 시나리오 1: Positive Funding =====
scenario1 = FancyBboxPatch((0.5, 4.3), 7, 3.0, 
                            boxstyle="round,pad=0.02,rounding_size=0.15",
                            facecolor='#FEF2F2', edgecolor=COLORS['danger'], 
                            linewidth=2)
ax.add_patch(scenario1)

ax.text(4, 7.0, 'SCENARIO 1: Perp > Spot', ha='center', fontsize=12, 
        fontweight='bold', color=COLORS['danger'])
ax.text(4, 6.5, 'Positive Funding Rate', ha='center', fontsize=10, 
        color=COLORS['danger'])

# Long -> Short
long1 = FancyBboxPatch((1.2, 4.8), 2, 1, 
                        boxstyle="round,pad=0.02,rounding_size=0.1",
                        facecolor='#FECACA', edgecolor=COLORS['danger'], linewidth=1.5)
ax.add_patch(long1)
ax.text(2.2, 5.3, 'LONG', ha='center', fontsize=11, fontweight='bold', 
        color=COLORS['danger'])

short1 = FancyBboxPatch((5.3, 4.8), 2, 1, 
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor='#BBF7D0', edgecolor=COLORS['success'], linewidth=1.5)
ax.add_patch(short1)
ax.text(6.3, 5.3, 'SHORT', ha='center', fontsize=11, fontweight='bold', 
        color=COLORS['success'])

ax.annotate('', xy=(5.1, 5.3), xytext=(3.4, 5.3),
            arrowprops=dict(arrowstyle='->', color=COLORS['danger'], lw=2.5))
ax.text(4.25, 5.8, 'Pays Funding', ha='center', fontsize=9, 
        fontweight='bold', color=COLORS['danger'])

# ===== 시나리오 2: Negative Funding =====
scenario2 = FancyBboxPatch((8.5, 4.3), 7, 3.0, 
                            boxstyle="round,pad=0.02,rounding_size=0.15",
                            facecolor='#F0FDF4', edgecolor=COLORS['success'], 
                            linewidth=2)
ax.add_patch(scenario2)

ax.text(12, 7.0, 'SCENARIO 2: Perp < Spot', ha='center', fontsize=12, 
        fontweight='bold', color=COLORS['success'])
ax.text(12, 6.5, 'Negative Funding Rate', ha='center', fontsize=10, 
        color=COLORS['success'])

# Short -> Long
short2 = FancyBboxPatch((9.2, 4.8), 2, 1, 
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor='#BBF7D0', edgecolor=COLORS['success'], linewidth=1.5)
ax.add_patch(short2)
ax.text(10.2, 5.3, 'SHORT', ha='center', fontsize=11, fontweight='bold', 
        color=COLORS['success'])

long2 = FancyBboxPatch((13.3, 4.8), 2, 1, 
                        boxstyle="round,pad=0.02,rounding_size=0.1",
                        facecolor='#FECACA', edgecolor=COLORS['danger'], linewidth=1.5)
ax.add_patch(long2)
ax.text(14.3, 5.3, 'LONG', ha='center', fontsize=11, fontweight='bold', 
        color=COLORS['danger'])

ax.annotate('', xy=(13.1, 5.3), xytext=(11.4, 5.3),
            arrowprops=dict(arrowstyle='->', color=COLORS['success'], lw=2.5))
ax.text(12.25, 5.8, 'Pays Funding', ha='center', fontsize=9, 
        fontweight='bold', color=COLORS['success'])

# ===== 하단: 정산 정보 =====
info_box = FancyBboxPatch((0.5, 0.5), 15, 3.5, 
                           boxstyle="round,pad=0.02,rounding_size=0.15",
                           facecolor=COLORS['light_gray'], 
                           edgecolor=COLORS['gray'], linewidth=1.5)
ax.add_patch(info_box)

ax.text(8, 3.7, 'FUNDING RATE DETAILS', ha='center', fontsize=12, 
        fontweight='bold', color=COLORS['dark'])
ax.plot([1, 15], [3.4, 3.4], color=COLORS['gray'], lw=0.5)

# 왼쪽: 계산 공식
ax.text(4.5, 3.0, 'Calculation Formula', ha='center', fontsize=11, 
        fontweight='bold', color=COLORS['dark'])
ax.text(4.5, 2.5, 'Funding Rate = Premium Index + clamp(IR - PI)', 
        ha='center', fontsize=10, style='italic')
ax.text(4.5, 2.0, 'Premium Index = (Perp - Spot) / Spot', ha='center', 
        fontsize=9, color=COLORS['gray'])
ax.text(4.5, 1.6, 'Interest Rate ≈ 0.01% (base)', ha='center', 
        fontsize=9, color=COLORS['gray'])

# 구분선
ax.plot([8, 8], [0.8, 3.2], color=COLORS['gray'], lw=0.5)

# 오른쪽: 정산 주기
ax.text(11.5, 3.0, 'Settlement Schedule', ha='center', fontsize=11, 
        fontweight='bold', color=COLORS['dark'])
ax.text(11.5, 2.5, 'Every 8 hours (00:00, 08:00, 16:00 UTC)', 
        ha='center', fontsize=10)
ax.text(11.5, 2.0, '3× daily = ~1,095× annually', ha='center', 
        fontsize=9, color=COLORS['gray'])
ax.text(11.5, 1.6, 'Avg Rate: ~0.01% (≈10.95% APY)', ha='center', 
        fontsize=9, color=COLORS['gray'])

# BACBB 관련
ax.text(8, 0.9, '→ In BACBB: Funding Rate is reflected as Trading Cost (f) in return calculation', 
        ha='center', fontsize=10, fontweight='bold', color=COLORS['primary'])

plt.tight_layout()
plt.savefig('Figure_Funding_Rate_Structure.png', dpi=250, bbox_inches='tight', 
            facecolor=COLORS['bg'], pad_inches=0.3)
plt.close()
print("  Figure_Funding_Rate_Structure.png 저장 완료")


print("\n" + "="*70)
print("프로페셔널 다이어그램 생성 완료!")
print("="*70)
print("\n생성된 파일:")
print("  1. Figure_BACBB_Logic_Flow.png")
print("  2. Figure_Campbell_Shiller_Decomposition.png")
print("  3. Figure_Funding_Rate_Structure.png")
