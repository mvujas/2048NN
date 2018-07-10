from experience_replay import ExperienceBuffer

a = ExperienceBuffer()
for i in range(10):
    a.add(i)
print(a)
print(a.get_batch(125))
