# generate_diagram.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Créer la figure
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Titre
plt.text(6, 7.5, 'ARCHITECTURE DU DÉTECTEUR DE FAKE NEWS', 
         fontsize=16, fontweight='bold', ha='center')

# Boîte 1: Texte d'entrée
ax.add_patch(patches.Rectangle((1, 5.5), 2, 1, fill=True, facecolor='lightblue'))
plt.text(2, 6, 'TEXTE INPUT\n"BREAKING: Free money\n giveaway! Share now!"', 
         fontsize=9, ha='center', va='center')

# Boîte 2: Prétraitement
ax.add_patch(patches.Rectangle((4, 5.5), 2, 1, fill=True, facecolor='lightgreen'))
plt.text(5, 6, 'PRÉTRAITEMENT\n• lowercase\n• remove URLs\n• stemming', 
         fontsize=9, ha='center', va='center')

# Boîte 3: Vectorisation
ax.add_patch(patches.Rectangle((7, 5.5), 2, 1, fill=True, facecolor='yellow'))
plt.text(8, 6, 'VECTORISATION\nTF-IDF (1-3 grams)\n5000 features', 
         fontsize=9, ha='center', va='center')

# Boîte 4: Classification
ax.add_patch(patches.Rectangle((10, 5.5), 2, 1, fill=True, facecolor='orange'))
plt.text(11, 6, 'CLASSIFICATION\nSVM Linéaire\nw⋅x + b = score', 
         fontsize=9, ha='center', va='center')

# Boîte 5: Résultat
ax.add_patch(patches.Rectangle((5.5, 2), 3, 1, fill=True, facecolor='red'))
plt.text(7, 2.5, '🚨 FAKE NEWS DÉTECTÉE\nConfiance: 91%', 
         fontsize=11, ha='center', va='center', color='white', fontweight='bold')

# Flèches
arrow_x = [3, 4, 9, 10, 7, 7]
arrow_y = [6, 6, 6, 6, 5.5, 3]
for i in range(0, len(arrow_x)-1, 2):
    ax.annotate('', xy=(arrow_x[i+1], arrow_y[i+1]), xytext=(arrow_x[i], arrow_y[i]),
                arrowprops=dict(arrowstyle='->', lw=2))

# Exemple détaillé
plt.text(2, 3.5, 'Exemple Features Importantes:\n• "urgent": +1.8\n• "free": +1.5\n• "money": +1.2\n• "share": +1.0', 
         fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcyan"))

plt.text(9, 3.5, 'Vecteur Résultat:\n[0.9, 1.2, 0.8, 1.5,\n0.0, 0.0, ..., 0.0]\n(5000 dimensions)', 
         fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))

plt.tight_layout()
plt.savefig('fake_news_architecture.png', dpi=300, bbox_inches='tight')
print("✅ Diagramme sauvegardé: fake_news_architecture.png")